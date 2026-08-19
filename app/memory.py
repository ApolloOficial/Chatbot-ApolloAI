"""Memória de curto e longo prazo persistida exclusivamente no MongoDB."""

from __future__ import annotations

import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Any

from pymongo import ASCENDING, DESCENDING, MongoClient
from pymongo.errors import PyMongoError

logger = logging.getLogger(__name__)


class MemoryUnavailable(RuntimeError):
    """Falha controlada de persistência sem revelar a URI."""


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def sanitize_for_storage(text: str) -> str:
    """Remove identificadores e credenciais comuns antes de persistir."""
    patterns = (
        (r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b", "[CPF OMITIDO]"),
        (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[E-MAIL OMITIDO]"),
        (r"(?i)\b(?:sk-|gsk_|AIza)[A-Za-z0-9_-]{12,}\b", "[CREDENCIAL OMITIDA]"),
        (r"(?i)(password|senha|token|api[_ -]?key)\s*[:=]\s*\S+", r"\1=[OMITIDO]"),
    )
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text


class MongoMemoryRepository:
    """Repositório multiusuário com sessões, mensagens, resumos e observabilidade."""

    def __init__(self, uri: str, database: str, timeout_ms: int = 1500, summary_after: int = 12,
                 max_context: int = 8, lookback_sessions: int = 3, retention_days: int = 180,
                 client=None) -> None:
        self.client = client or MongoClient(
            uri, serverSelectionTimeoutMS=timeout_ms, connectTimeoutMS=timeout_ms,
            appname="ApolloAI", tz_aware=True,
        )
        self.db = self.client[database]
        self.sessions = self.db["sessions"]
        self.messages = self.db["messages"]
        self.long_term = self.db["long_term_memories"]
        self.summaries = self.db["summaries"]
        self.observability = self.db["observability"]
        self.summary_after = summary_after
        self.max_context = max_context
        self.lookback_sessions = lookback_sessions
        self.retention_days = retention_days
        self._indexes_ready = False

    @classmethod
    def from_config(cls, config):
        return cls(
            config["MONGODB_URI"], config["MONGODB_DATABASE"], config["MONGODB_TIMEOUT_MS"],
            config["SUMMARY_AFTER_MESSAGES"], config["MAX_CONTEXT_MESSAGES"],
            config["MEMORY_LOOKBACK_SESSIONS"], config["RETENTION_DAYS"],
        )

    def ensure_indexes(self) -> None:
        if self._indexes_ready:
            return
        try:
            self.sessions.create_index([("user_id", ASCENDING), ("session_id", ASCENDING)], unique=True)
            self.sessions.create_index("updated_at")
            self.messages.create_index([("user_id", ASCENDING), ("session_id", ASCENDING), ("created_at", ASCENDING)])
            self.messages.create_index("expires_at", expireAfterSeconds=0)
            self.long_term.create_index([("user_id", ASCENDING), ("created_at", DESCENDING)])
            self.summaries.create_index([("user_id", ASCENDING), ("created_at", DESCENDING)])
            self.observability.create_index("created_at")
            self._indexes_ready = True
        except PyMongoError as error:
            self._raise(error)

    def health(self) -> str:
        try:
            self.client.admin.command("ping")
            self.ensure_indexes()
            return "disponivel"
        except Exception:
            return "indisponivel"

    def start_session(self, user_id: str, session_id: str) -> None:
        self.ensure_indexes()
        now = utcnow()
        try:
            self.sessions.update_one(
                {"user_id": user_id, "session_id": session_id},
                {"$setOnInsert": {
                    "user_id": user_id, "session_id": session_id, "created_at": now,
                    "status": "ativa", "summary": "", "messages": [], "agents_called": [],
                    "last_route": "fora_escopo", "message_count": 0,
                }, "$set": {"updated_at": now}}, upsert=True,
            )
        except PyMongoError as error:
            self._raise(error)

    def verify_ownership(self, user_id: str, session_id: str) -> bool:
        try:
            owner = self.sessions.find_one({"session_id": session_id}, {"user_id": 1})
            return owner is None or owner.get("user_id") == user_id
        except PyMongoError as error:
            self._raise(error)

    def context(self, user_id: str, session_id: str, question: str) -> tuple[list[dict], list[dict]]:
        try:
            recent = list(self.messages.find(
                {"user_id": user_id, "session_id": session_id}, {"_id": 0, "role": 1, "content": 1}
            ).sort("created_at", DESCENDING).limit(self.max_context))[::-1]
            candidates = list(self.summaries.find(
                {"user_id": user_id, "session_id": {"$ne": session_id}},
                {"_id": 0, "session_id": 1, "summary": 1, "created_at": 1},
            ).sort("created_at", DESCENDING).limit(self.lookback_sessions * 3))
            query_terms = _terms(question)
            relevant = [item for item in candidates if query_terms & _terms(item.get("summary", ""))]
            return recent, relevant[: self.lookback_sessions]
        except PyMongoError as error:
            self._raise(error)

    def save_message(self, user_id: str, session_id: str, role: str, content: str, **metadata) -> None:
        now = utcnow()
        message = {
            "user_id": user_id, "session_id": session_id, "role": role,
            "content": sanitize_for_storage(content), "created_at": now,
            "expires_at": now + timedelta(days=self.retention_days),
            "route": metadata.get("route"), "agents_called": metadata.get("agents_called", []),
            "sources": metadata.get("sources", []), "judge_decision": metadata.get("judge_decision", {}),
            "blocked": metadata.get("blocked", False), "block_reason": metadata.get("block_reason"),
            "total_latency_ms": metadata.get("total_latency_ms", 0),
        }
        try:
            self.messages.insert_one(message)
            bounded = {key: value for key, value in message.items() if key not in {"_id", "user_id", "session_id", "expires_at"}}
            self.sessions.update_one(
                {"user_id": user_id, "session_id": session_id},
                {"$push": {"messages": {"$each": [bounded], "$slice": -self.max_context}},
                 "$inc": {"message_count": 1}, "$set": {"updated_at": now},
                 "$addToSet": {"agents_called": {"$each": metadata.get("agents_called", [])}}},
            )
        except PyMongoError as error:
            self._raise(error)

    def update_session_result(self, user_id: str, session_id: str, route: str) -> None:
        try:
            self.sessions.update_one(
                {"user_id": user_id, "session_id": session_id},
                {"$set": {"last_route": route, "updated_at": utcnow()}},
            )
        except PyMongoError as error:
            self._raise(error)

    def maybe_summarize(self, user_id: str, session_id: str) -> None:
        try:
            session = self.sessions.find_one({"user_id": user_id, "session_id": session_id}) or {}
            count = int(session.get("message_count", 0))
            if count == 0 or count % self.summary_after:
                return
            messages = list(self.messages.find(
                {"user_id": user_id, "session_id": session_id}, {"role": 1, "content": 1}
            ).sort("created_at", DESCENDING).limit(self.summary_after))[::-1]
            summary = _deterministic_summary(messages)
            now = utcnow()
            self.summaries.update_one(
                {"user_id": user_id, "session_id": session_id},
                {"$set": {"summary": summary, "updated_at": now}, "$setOnInsert": {"created_at": now}},
                upsert=True,
            )
            self.sessions.update_one(
                {"user_id": user_id, "session_id": session_id}, {"$set": {"summary": summary}},
            )
        except PyMongoError as error:
            self._raise(error)

    def close_session(self, user_id: str, session_id: str) -> None:
        self.maybe_summarize(user_id, session_id)
        try:
            self.sessions.update_one(
                {"user_id": user_id, "session_id": session_id},
                {"$set": {"status": "encerrada", "updated_at": utcnow()}},
            )
        except PyMongoError as error:
            self._raise(error)

    def save_observation(self, record: dict[str, Any]) -> None:
        safe = {key: value for key, value in record.items() if key not in {"user_id", "session_id", "question", "answer"}}
        safe["created_at"] = utcnow()
        try:
            self.observability.insert_one(safe)
        except PyMongoError as error:
            self._raise(error)

    @staticmethod
    def _raise(error: Exception):
        logger.warning("mongodb_indisponivel", extra={"error_type": type(error).__name__})
        raise MemoryUnavailable("Não foi possível persistir a conversa no momento.") from error


def _terms(text: str) -> set[str]:
    return {term for term in re.findall(r"[a-zà-ÿ]{4,}", text.lower()) if term not in {"sobre", "como", "para", "qual", "quais"}}


def _deterministic_summary(messages: list[dict]) -> str:
    snippets = []
    for message in messages[-6:]:
        content = sanitize_for_storage(message.get("content", "")).replace("\n", " ")[:180]
        snippets.append(f"{message.get('role', 'mensagem')}: {content}")
    return " | ".join(snippets)[:1000]
