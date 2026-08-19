"""Endpoint do chatbot ApolloAI."""

from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.extensions import get_service
from app.schemas import ChatRequest, public_validation_errors
from app.services.chat_service import SessionAccessDenied

chat_bp = Blueprint("chat", __name__)


@chat_bp.post("/chat")
def chat():
    try:
        payload = ChatRequest.model_validate(request.get_json(silent=True) or {})
    except ValidationError as error:
        return jsonify({"status": "erro", "erro": "Payload inválido.", "detalhes": public_validation_errors(error.errors())}), 422

    try:
        response = get_service(current_app, "chat").execute(payload)
    except SessionAccessDenied:
        return jsonify({
            "session_id": payload.session_id, "resposta": "A sessão informada não pertence a este usuário.",
            "status": "erro", "rota": "fora_escopo", "agentes_chamados": [], "fontes": [],
            "alerta_seguranca": None, "motivo_bloqueio": "acesso_sessao_negado",
        }), 403
    status_code = 503 if response.status == "erro" else 200
    return jsonify(response.model_dump(mode="json")), status_code
