"""Configuração centralizada, sem conexão com PostgreSQL."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _csv(name: str, default: str) -> list[str]:
    return [item.strip() for item in os.getenv(name, default).split(",") if item.strip()]


class Config:
    APP_NAME = "ApolloAI"
    VERSION = "1.0.0"
    JSON_AS_ASCII = False
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", "32768"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    CORS_ORIGINS = _csv("CORS_ORIGINS", "http://localhost:5000,http://localhost")
    AUTH_REQUIRED = os.getenv("AUTH_REQUIRED", "false").lower() == "true"
    APOLLOAI_API_TOKEN = os.getenv("APOLLOAI_API_TOKEN")
    FRONTEND_DIR = BASE_DIR / "frontend"
    SOLAR_DATA_DIR = BASE_DIR / "data" / "solar"
    SOLAR_DOCUMENTS_DIR = SOLAR_DATA_DIR / "documentos"
    VECTOR_INDEX_PATH = SOLAR_DATA_DIR / "indice.json"

    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "apollo_ai")
    MONGODB_TIMEOUT_MS = int(os.getenv("MONGODB_TIMEOUT_MS", "1500"))
    MONGODB_REQUIRED = os.getenv("MONGODB_REQUIRED", "true").lower() == "true"
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    REDIS_ENABLED = os.getenv("REDIS_ENABLED", "true").lower() == "true"

    AI_PROVIDER = os.getenv("AI_PROVIDER", "groq")
    AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-oss-120b")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    AI_TIMEOUT_SECONDS = float(os.getenv("AI_TIMEOUT_SECONDS", "30"))
    AI_MAX_RETRIES = int(os.getenv("AI_MAX_RETRIES", "1"))

    MCP_TRANSPORT = os.getenv("MCP_TRANSPORT", "stdio")
    MCP_TIMEOUT_SECONDS = float(os.getenv("MCP_TIMEOUT_SECONDS", "12"))
    MCP_SERVER_COMMAND = os.getenv("MCP_SERVER_COMMAND", "python -m app.mcp_server")
    RAG_TOP_K = int(os.getenv("RAG_TOP_K", "5"))
    RAG_MIN_SCORE = float(os.getenv("RAG_MIN_SCORE", "0.08"))

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
    PERSISTENCE_BACKEND = "mongodb"
