"""Endpoint de saúde sem dados sensíveis."""

from flask import Blueprint, current_app, jsonify

from app.extensions import get_service

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    memory = get_service(current_app, "memory")
    rag = get_service(current_app, "rag")
    redis = get_service(current_app, "redis")
    mongo_state = memory.health()
    payload = {
        "status": "ok" if mongo_state == "disponivel" and rag.is_ready else "degradado",
        "servico": "ApolloAI",
        "versao": current_app.config["VERSION"],
        "mongodb": mongo_state,
        "rag": "disponivel" if rag.is_ready else "nao_indexado",
        "mcp": "configurado",
        "redis": redis.health(),
    }
    return jsonify(payload), 200 if payload["status"] == "ok" else 503
