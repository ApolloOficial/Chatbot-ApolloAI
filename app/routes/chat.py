"""Endpoint do chatbot ApolloAI."""

from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.extensions import get_service
from app.schemas import ChatRequest, public_validation_errors

chat_bp = Blueprint("chat", __name__)


@chat_bp.post("/chat")
def chat():
    try:
        payload = ChatRequest.model_validate(request.get_json(silent=True) or {})
    except ValidationError as error:
        return jsonify({"status": "erro", "erro": "Payload inválido.", "detalhes": public_validation_errors(error.errors())}), 422

    response = get_service(current_app, "chat").execute(payload)
    status_code = 503 if response.status == "erro" else 200
    return jsonify(response.model_dump(mode="json")), status_code
