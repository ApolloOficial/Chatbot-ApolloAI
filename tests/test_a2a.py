from __future__ import annotations


def _request(payload, **overrides):
    message = {
        "messageId": "msg-001",
        "contextId": payload["session_id"],
        "role": "ROLE_USER",
        "parts": [{"text": payload["pergunta"]}],
        "metadata": {"userId": payload["user_id"], "contexto": payload["contexto"]},
    }
    message.update(overrides)
    return {"jsonrpc": "2.0", "id": "rpc-001", "method": "SendMessage", "params": {"message": message}}


def test_agent_card_declares_a2a_1_protocol(client):
    response = client.get("/.well-known/agent-card.json")
    assert response.status_code == 200
    assert response.json["supportedInterfaces"][0]["protocolBinding"] == "JSONRPC"
    assert response.json["supportedInterfaces"][0]["protocolVersion"] == "1.0"
    assert len(response.json["skills"]) == 2
    assert response.headers["Cache-Control"] == "public, max-age=3600"


def test_a2a_send_message_executes_apolloai_graph(client, payload):
    response = client.post("/a2a/v1", json=_request(payload), headers={"A2A-Version": "1.0"})
    assert response.status_code == 200
    message = response.json["result"]["message"]
    assert message["role"] == "ROLE_AGENT"
    assert message["contextId"] == payload["session_id"]
    assert message["parts"][0]["text"]
    assert message["parts"][1]["data"]["route"] == "ativos_solares"


def test_a2a_rejects_unknown_method(client):
    response = client.post("/a2a/v1", json={"jsonrpc": "2.0", "id": 1, "method": "DeleteEverything"})
    assert response.json["error"]["code"] == -32601


def test_a2a_rejects_non_text_parts(client, payload):
    response = client.post("/a2a/v1", json=_request(payload, parts=[{"data": {"unsafe": True}}]))
    assert response.json["error"]["code"] == -32602


def test_a2a_authenticated_mode_uses_trusted_header(app_bundle, payload):
    app_bundle[0].config.update(AUTH_REQUIRED=True, APOLLOAI_API_TOKEN="test-service-token")
    client = app_bundle[0].test_client()
    headers = {
        "Authorization": "Bearer test-service-token", "X-User-ID": payload["user_id"], "A2A-Version": "1.0",
    }
    assert client.post("/a2a/v1", json=_request(payload)).status_code == 401
    assert client.post("/a2a/v1", json=_request(payload), headers=headers).status_code == 200
