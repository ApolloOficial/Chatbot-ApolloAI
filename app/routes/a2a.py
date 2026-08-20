"""Descoberta e transporte JSON-RPC do protocolo A2A 1.0."""

from __future__ import annotations

from flask import Blueprint, current_app, jsonify, request
from pydantic import ValidationError

from app.a2a import A2A_VERSION, SendMessageParams, agent_card, response_message
from app.auth import AuthenticationRequired, TrustedIdentityRequired, trusted_user_id
from app.extensions import get_service
from app.services.chat_service import SessionAccessDenied

a2a_bp = Blueprint("a2a", __name__)


def _error(request_id, code: int, message: str, data=None):
    payload = {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}
    if data:
        payload["error"]["data"] = data
    return jsonify(payload)


@a2a_bp.get("/.well-known/agent-card.json")
def public_agent_card():
    base_url = current_app.config.get("PUBLIC_BASE_URL") or request.url_root
    payload = agent_card(base_url, current_app.config["VERSION"], current_app.config["AUTH_REQUIRED"])
    response = jsonify(payload)
    response.headers["Cache-Control"] = "public, max-age=3600"
    response.headers["ETag"] = f'"apolloai-{current_app.config["VERSION"]}"'
    return response


@a2a_bp.post("/a2a/v1")
def jsonrpc_endpoint():
    rpc = request.get_json(silent=True)
    if not isinstance(rpc, dict):
        return _error(None, -32700, "Invalid JSON payload")
    request_id = rpc.get("id")
    if rpc.get("jsonrpc") != "2.0" or "id" not in rpc or not isinstance(rpc.get("method"), str):
        return _error(request_id, -32600, "Request payload validation error")
    if request.headers.get("A2A-Version", A2A_VERSION) != A2A_VERSION:
        return _error(request_id, -32602, "Unsupported A2A version")
    if rpc["method"] != "SendMessage":
        return _error(request_id, -32601, "Method not found")

    try:
        identity = trusted_user_id(request, current_app.config)
    except (AuthenticationRequired, TrustedIdentityRequired):
        return _error(request_id, -32001, "Authentication required"), 401
    try:
        params = SendMessageParams.model_validate(rpc.get("params", {}))
        chat_request = params.to_chat_request(identity)
    except (ValidationError, ValueError) as error:
        details = error.errors(include_url=False) if isinstance(error, ValidationError) else [{"message": str(error)}]
        return _error(request_id, -32602, "Invalid parameters", details)

    try:
        chat_response = get_service(current_app, "chat").execute(chat_request)
    except SessionAccessDenied:
        return _error(request_id, -32003, "Context belongs to another identity"), 403
    result = {"message": response_message(chat_response, chat_request.session_id)}
    return jsonify({"jsonrpc": "2.0", "id": request_id, "result": result})
