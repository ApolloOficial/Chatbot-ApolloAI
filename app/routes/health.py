"""Endpoints de liveness e disponibilidade das integrações."""

from flask import Blueprint, current_app, jsonify

from app.extensions import get_service
from app.services.neo4j_service import Neo4jUnavailable

health_bp = Blueprint("health", __name__)


@health_bp.get("/live")
def live():
    """Responde sem consultar dependências externas."""
    return jsonify({"status": "ok", "servico": "ApolloAI", "versao": current_app.config["VERSION"]})


@health_bp.get("/health")
def health():
    memory = get_service(current_app, "memory")
    rag = get_service(current_app, "rag")
    redis = get_service(current_app, "redis")
    mcp = get_service(current_app, "mcp")
    mongo_state = memory.health()
    redis_state = redis.health()
    mcp_state = mcp.health()
    rag_ready = rag.is_ready
    neo4j_config = [current_app.config.get(name) for name in ("NEO4J_URI", "NEO4J_USER", "NEO4J_PASSWORD")]
    neo4j_state = "nao_configurado" if not any(neo4j_config) else "indisponivel"
    if all(neo4j_config):
        try:
            get_service(current_app, "knowledge_graph").paths_for_component("Cabo")
            neo4j_state = "disponivel"
        except Neo4jUnavailable:
            pass
    essential_states = [mongo_state == "disponivel", rag_ready]
    if current_app.config["REDIS_REQUIRED"]:
        essential_states.append(redis_state == "disponivel")
    if current_app.config["MCP_REQUIRED"]:
        essential_states.append(mcp_state == "disponivel")
    payload = {
        "status": "ok" if all(essential_states) else "degradado",
        "servico": "ApolloAI",
        "versao": current_app.config["VERSION"],
        "mongodb": mongo_state,
        "rag": "disponivel" if rag_ready else "indisponivel",
        "mcp": mcp_state,
        "redis": redis_state,
        "neo4j": neo4j_state,
    }
    return jsonify(payload), 200 if payload["status"] == "ok" else 503
