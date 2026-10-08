"""Consulta de negócio demonstrando traversal no Neo4j."""

from flask import Blueprint, current_app, jsonify, request

from app.auth import AuthenticationRequired, TrustedIdentityRequired, trusted_user_id
from app.extensions import get_service
from app.services.neo4j_service import Neo4jUnavailable

knowledge_graph_bp = Blueprint("knowledge_graph", __name__)


@knowledge_graph_bp.get("/knowledge/impact")
def component_impact():
    try:
        trusted_user_id(request, current_app.config)
    except (AuthenticationRequired, TrustedIdentityRequired):
        return jsonify({"status": "erro", "erro": "Autenticação obrigatória."}), 401
    component = request.args.get("componente", "").strip()
    if not 2 <= len(component) <= 120:
        return jsonify({"status": "erro", "erro": "Informe um componente entre 2 e 120 caracteres."}), 422
    try:
        paths = get_service(current_app, "knowledge_graph").paths_for_component(component)
    except Neo4jUnavailable:
        return jsonify({"status": "erro", "erro": "Grafo Neo4j indisponível."}), 503
    return jsonify({"componente": component, "caminhos": paths, "total": len(paths)})
