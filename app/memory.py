"""Sessões e mensagens no MongoDB com recuperação semântica de resumos no Qdrant."""

from __future__ import annotations

import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Any

from pymongo import ASCENDING, DESCENDING, MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError

from app.qdrant_store import QdrantSemanticStore, QdrantUnavailable

logger = logging.getLogger(__name__)


class MemoryUnavailable(RuntimeError):
    """Falha controlada de persistência sem revelar a URI."""


class SessionClosed(RuntimeError):
    """Uma sessão encerrada não pode receber novos turnos."""


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
                 client=None, semantic_store: QdrantSemanticStore | None = None) -> None:
        self.client = client or MongoClient(
            uri, serverSelectionTimeoutMS=timeout_ms, connectTimeoutMS=timeout_ms,
            appname="ApolloAI", tz_aware=True,
        )
        self.db = self.client[database]
        self.sessions = self.db["sessions"]
        self.messages = self.db["messages"]
        self.summaries = self.db["summaries"]
        self.observability = self.db["observability"]
        self.summary_after = summary_after
        self.max_context = max_context
        self.lookback_sessions = lookback_sessions
        self.retention_days = retention_days
        self.semantic_store = semantic_store
        self._indexes_ready = False

    @classmethod
    def from_config(cls, config):
        return cls(
            config["MONGODB_URI"], config["MONGODB_DATABASE"], config["MONGODB_TIMEOUT_MS"],
            config["SUMMARY_AFTER_MESSAGES"], config["MAX_CONTEXT_MESSAGES"],
            config["MEMORY_LOOKBACK_SESSIONS"], config["RETENTION_DAYS"],
            semantic_store=QdrantSemanticStore.from_config(config),
        )

    def ensure_indexes(self) -> None:
        if self._indexes_ready:
            return
        try:
            self.sessions.create_index([("user_id", ASCENDING), ("session_id", ASCENDING)], unique=True)
            self.sessions.create_index("updated_at")
            self.messages.create_index([("user_id", ASCENDING), ("session_id", ASCENDING), ("created_at", ASCENDING)])
            self.messages.create_index("expires_at", expireAfterSeconds=0)
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
                {"user_id": user_id, "session_id": session_id, "status": {"$ne": "encerrada"}},
                {"$setOnInsert": {
                    "user_id": user_id, "session_id": session_id, "created_at": now,
                    "status": "ativa", "summary": "", "message_count": 0,
                }, "$set": {"updated_at": now}}, upsert=True,
            )
        except DuplicateKeyError as error:
            try:
                session = self.sessions.find_one({"user_id": user_id, "session_id": session_id}, {"status": 1})
            except PyMongoError as lookup_error:
                self._raise(lookup_error)
            if session and session.get("status") != "encerrada":
                return
            raise SessionClosed from error
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
            return recent, self._semantic_summaries(user_id, session_id, question)
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
            self.sessions.update_one(
                {"user_id": user_id, "session_id": session_id},
                {"$inc": {"message_count": 1}, "$set": {"updated_at": now}},
            )
        except PyMongoError as error:
            self._raise(error)

    def maybe_summarize(self, user_id: str, session_id: str, force: bool = False) -> None:
        try:
            session = self.sessions.find_one({"user_id": user_id, "session_id": session_id}) or {}
            count = int(session.get("message_count", 0))
            if count == 0 or (not force and count % self.summary_after):
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
            self._index_summary(user_id, session_id, summary, now)
        except PyMongoError as error:
            self._raise(error)

    def close_session(self, user_id: str, session_id: str) -> None:
        self.maybe_summarize(user_id, session_id, force=True)
        try:
            self.sessions.update_one(
                {"user_id": user_id, "session_id": session_id},
                {"$set": {"status": "encerrada", "updated_at": utcnow()}},
            )
        except PyMongoError as error:
            self._raise(error)

    def save_observation(self, record: dict[str, Any]) -> None:
        fields = ("route", "agents_called", "blocked", "block_reason", "total_latency_ms",
                  "agent_latencies_ms", "source_count")
        safe = {key: record[key] for key in fields if key in record}
        decision = record.get("judge_decision") or {}
        safe["judge_decision"] = {key: decision[key] for key in (
            "decisao", "fundamentada", "segura", "dentro_escopo", "fontes_validas",
            "hipotese_como_diagnostico",
        ) if key in decision}
        safe["created_at"] = utcnow()
        try:
            self.observability.insert_one(safe)
        except PyMongoError as error:
            self._raise(error)

    @staticmethod
    def _raise(error: Exception):
        logger.warning("mongodb_indisponivel", extra={"error_type": type(error).__name__})
        raise MemoryUnavailable("Não foi possível persistir a conversa no momento.") from error
    def _index_summary(self, user_id: str, session_id: str, summary: str, created_at: datetime) -> None:
        if not self.semantic_store or not self.semantic_store.configured:
            raise QdrantUnavailable("Qdrant remoto não configurado para memória.")
        try:
            self.semantic_store.upsert_summary(user_id, session_id, summary, created_at.isoformat())
        except Exception as error:
            logger.warning("qdrant_resumo_nao_indexado", extra={"error_type": type(error).__name__})
            raise QdrantUnavailable("Não foi possível indexar o resumo no Qdrant.") from error

    def _semantic_summaries(self, user_id: str, session_id: str, question: str) -> list[dict]:
        if not question:
            return []
        if not self.semantic_store or not self.semantic_store.configured:
            raise QdrantUnavailable("Qdrant remoto não configurado para memória.")
        try:
            matches = self.semantic_store.search_summaries(user_id, question, self.lookback_sessions + 1)
            return [
                {"session_id": item.get("session_id"), "summary": item.get("resumo", ""),
                 "created_at": item.get("created_at"), "score": item.get("score")}
                for item in matches if item.get("session_id") != session_id and item.get("resumo")
            ][:self.lookback_sessions]
        except Exception as error:
            logger.warning("qdrant_memoria_indisponivel", extra={"error_type": type(error).__name__})
            raise QdrantUnavailable("Não foi possível recuperar a memória no Qdrant.") from error


def _deterministic_summary(messages: list[dict]) -> str:
    snippets = []
    for message in messages[-6:]:
        content = sanitize_for_storage(message.get("content", "")).replace("\n", " ")[:180]
        snippets.append(f"{message.get('role', 'mensagem')}: {content}")
    return " | ".join(snippets)[:1000]
