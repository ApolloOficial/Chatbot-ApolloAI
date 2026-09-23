"""Configuração centralizada, sem conexão com PostgreSQL."""

from __future__ import annotations

import os
import ipaddress
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _csv(name: str, default: str) -> list[str]:
    return [item.strip() for item in os.getenv(name, default).split(",") if item.strip()]


def is_local_hostname(hostname: str | None) -> bool:
    if not hostname:
        return True
    name = hostname.lower()
    if name in {"localhost", "host.docker.internal", "mongo", "redis", "qdrant"} or name.endswith((".localhost", ".local")):
        return True
    try:
        address = ipaddress.ip_address(name)
    except ValueError:
        return False
    return address.is_loopback or address.is_link_local or address.is_unspecified


class Config:
    VERSION = "1.0.0"
    PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", "32768"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    CORS_ORIGINS = _csv("CORS_ORIGINS", "")
    AUTH_REQUIRED = os.getenv("AUTH_REQUIRED", "true").lower() == "true"
    APOLLOAI_API_TOKEN = os.getenv("APOLLOAI_API_TOKEN")
    FRONTEND_DIR = BASE_DIR / "frontend"
    SOLAR_DATA_DIR = BASE_DIR / "data" / "solar"
    SOLAR_DOCUMENTS_DIR = SOLAR_DATA_DIR / "documentos"

    MONGODB_URI = os.getenv("MONGODB_URI")
    MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "apollo_ai")
    MONGODB_TIMEOUT_MS = int(os.getenv("MONGODB_TIMEOUT_MS", "1500"))
    MONGODB_REQUIRED = os.getenv("MONGODB_REQUIRED", "true").lower() == "true"
    REDIS_URL = os.getenv("REDIS_URL")
    REDIS_ENABLED = os.getenv("REDIS_ENABLED", "true").lower() == "true"
    REDIS_REQUIRED = os.getenv("REDIS_REQUIRED", "true").lower() == "true"
    REDIS_TIMEOUT_SECONDS = float(os.getenv("REDIS_TIMEOUT_SECONDS", "5"))

    AI_PROVIDER = os.getenv("AI_PROVIDER", "bedrock")
    AI_MODEL = os.getenv("AI_MODEL", "")
    AWS_REGION = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    AI_TIMEOUT_SECONDS = float(os.getenv("AI_TIMEOUT_SECONDS", "30"))
    AI_MAX_RETRIES = int(os.getenv("AI_MAX_RETRIES", "1"))

    MCP_REQUIRED = os.getenv("MCP_REQUIRED", "true").lower() == "true"
    MCP_TIMEOUT_SECONDS = float(os.getenv("MCP_TIMEOUT_SECONDS", "12"))
    MCP_SERVER_COMMAND = os.getenv("MCP_SERVER_COMMAND", "python -m app.mcp_server")
    RAG_TOP_K = int(os.getenv("RAG_TOP_K", "5"))
    RAG_MIN_SCORE = float(os.getenv("RAG_MIN_SCORE", "0.08"))
    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_VECTOR_SIZE = int(os.getenv("QDRANT_VECTOR_SIZE", "768"))
    QDRANT_INDEX_BATCH_SIZE = int(os.getenv("QDRANT_INDEX_BATCH_SIZE", "50"))
    QDRANT_TIMEOUT_SECONDS = float(os.getenv("QDRANT_TIMEOUT_SECONDS", "10"))

    SUMMARY_AFTER_MESSAGES = int(os.getenv("SUMMARY_AFTER_MESSAGES", "12"))
    MAX_CONTEXT_MESSAGES = int(os.getenv("MAX_CONTEXT_MESSAGES", "8"))
    MEMORY_LOOKBACK_SESSIONS = int(os.getenv("MEMORY_LOOKBACK_SESSIONS", "3"))
    RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "180"))

    PRICE_INPUT_PER_MILLION = float(os.getenv("PRICE_INPUT_PER_MILLION", "0"))
    PRICE_OUTPUT_PER_MILLION = float(os.getenv("PRICE_OUTPUT_PER_MILLION", "0"))
    AVG_MESSAGES_PER_USER = float(os.getenv("AVG_MESSAGES_PER_USER", "5"))
    AVG_INPUT_TOKENS = float(os.getenv("AVG_INPUT_TOKENS", "700"))
    AVG_OUTPUT_TOKENS = float(os.getenv("AVG_OUTPUT_TOKENS", "350"))
    AVG_AGENTS_PER_REQUEST = float(os.getenv("AVG_AGENTS_PER_REQUEST", "4"))
    AVG_RAG_QUERIES = float(os.getenv("AVG_RAG_QUERIES", "1"))
    ESTIMATED_RESOLUTION_RATE = float(os.getenv("ESTIMATED_RESOLUTION_RATE", "0.75"))
    ESTIMATED_MINUTES_SAVED = float(os.getenv("ESTIMATED_MINUTES_SAVED", "5"))
    TECHNICIAN_HOURLY_COST = float(os.getenv("TECHNICIAN_HOURLY_COST", "0"))

    TESTING = False


def validate_remote_config(config) -> None:
    if config.get("TESTING"):
        return

    def remote_url(name: str, schemes: set[str]) -> None:
        parsed = urlparse(config.get(name) or "")
        if parsed.scheme not in schemes or is_local_hostname(parsed.hostname):
            raise ValueError(f"{name} deve apontar para um serviço remoto com protocolo seguro.")

    remote_url("PUBLIC_BASE_URL", {"https"})
    remote_url("QDRANT_URL", {"https"})
    remote_url("MONGODB_URI", {"mongodb", "mongodb+srv"})
    remote_url("REDIS_URL", {"rediss"})
    origins = config.get("CORS_ORIGINS") or []
    if not origins:
        raise ValueError("CORS_ORIGINS deve conter ao menos uma origem HTTPS.")
    for origin in origins:
        parsed = urlparse(origin)
        if parsed.scheme != "https" or is_local_hostname(parsed.hostname):
            raise ValueError("CORS_ORIGINS deve conter somente origens HTTPS remotas.")
    for name in ("QDRANT_API_KEY", "APOLLOAI_API_TOKEN", "AI_MODEL"):
        if not config.get(name):
            raise ValueError(f"{name} é obrigatório.")
    for name in ("AUTH_REQUIRED", "MONGODB_REQUIRED", "REDIS_ENABLED", "REDIS_REQUIRED", "MCP_REQUIRED"):
        if not config.get(name):
            raise ValueError(f"{name} deve estar habilitado.")
    provider = (config.get("AI_PROVIDER") or "").lower()
    if provider == "bedrock":
        if not config.get("AWS_REGION"):
            raise ValueError("AWS_REGION é obrigatório para Claude via Amazon Bedrock.")
    elif provider == "groq":
        if not config.get("GROQ_API_KEY"):
            raise ValueError("GROQ_API_KEY é obrigatória para Groq.")
    elif provider in {"google", "gemini"}:
        if not config.get("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY é obrigatória para Gemini.")
    else:
        raise ValueError("AI_PROVIDER não suportado.")
