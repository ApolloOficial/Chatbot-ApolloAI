"""Ciclo de vida explícito das sessões conversacionais."""

from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.auth import AuthenticationRequired, TrustedIdentityRequired, trusted_user_id
from app.extensions import get_service
from app.memory import MemoryUnavailable
from app.schemas import SessionCloseRequest, public_validation_errors

sessions_bp = Blueprint("sessions", __name__)


@sessions_bp.post("/sessions/<session_id>/close")
def close_session(session_id: str):
    raw_payload = request.get_json(silent=True) or {}
    try:
        identity = trusted_user_id(request, current_app.config, raw_payload.get("user_id"))
    except AuthenticationRequired:
        return jsonify({"status": "erro", "erro": "Autenticação obrigatória."}), 401
    except TrustedIdentityRequired:
        return jsonify({"status": "erro", "erro": "Identidade confiável obrigatória."}), 401
    if identity is not None:
        raw_payload["user_id"] = identity
    try:
        payload = SessionCloseRequest.model_validate(raw_payload)
    except ValidationError as error:
        return jsonify({
            "status": "erro", "erro": "Payload inválido.", "detalhes": public_validation_errors(error.errors()),
        }), 422

    memory = get_service(current_app, "memory")
    try:
        if not memory.verify_ownership(payload.user_id, session_id):
            return jsonify({"status": "erro", "erro": "A sessão informada não pertence a este usuário."}), 403
        memory.close_session(payload.user_id, session_id)
    except MemoryUnavailable:
        return jsonify({"status": "erro", "erro": "Não foi possível encerrar a sessão."}), 503
    return jsonify({"status": "sucesso", "session_id": session_id})
