"""Endpoint de saúde sem dados sensíveis."""

from flask import Blueprint, current_app, jsonify

from app.extensions import get_service

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    memory = get_service(current_app, "memory")
    rag = get_service(current_app, "rag")
    redis = get_service(current_app, "redis")
    mcp = get_service(current_app, "mcp")
    mongo_state = memory.health()
    redis_state = redis.health()
    mcp_state = mcp.health()
    essential_states = [mongo_state == "disponivel", rag.is_ready]
    if current_app.config["REDIS_REQUIRED"]:
        essential_states.append(redis_state == "disponivel")
    if current_app.config["MCP_REQUIRED"]:
        essential_states.append(mcp_state == "disponivel")
    payload = {
        "status": "ok" if all(essential_states) else "degradado",
        "servico": "ApolloAI",
        "versao": current_app.config["VERSION"],
        "mongodb": mongo_state,
        "rag": "disponivel" if rag.is_ready else "nao_indexado",
        "mcp": mcp_state,
        "redis": redis_state,
    }
    return jsonify(payload), 200 if payload["status"] == "ok" else 503
