from __future__ import annotations


def test_sessions_are_isolated_by_user(client, payload):
    assert client.post("/chat", json=payload).status_code == 200
    response = client.post("/chat", json={**payload, "user_id": "outro-tecnico"})
    assert response.status_code == 403


def test_messages_route_agents_and_judge_are_saved(client, payload, app_bundle):
    client.post("/chat", json=payload)
    memory = app_bundle[1]
    assert memory.messages.count_documents({"user_id": payload["user_id"]}) == 2
    assistant = memory.messages.find_one({"role": "assistente"})
    assert assistant["route"] == "ativos_solares"
    assert "juiz_factual" in assistant["agents_called"]
    assert assistant["judge_decision"]["decisao"] == "aprovada"


def test_previous_message_is_recovered_into_context(client, payload, app_bundle):
    client.post("/chat", json=payload)
    client.post("/chat", json={**payload, "pergunta": "Obrigado ApolloAI"})
    faq_calls = [content for name, content in app_bundle[2].calls if name == "faq_apolloai"]
    assert any("reduzir a eficiência" in content for content in faq_calls)


def test_summary_is_generated_at_configured_limit(client, payload, app_bundle):
    client.post("/chat", json=payload)
    client.post("/chat", json={**payload, "pergunta": "Obrigado ApolloAI"})
    assert app_bundle[1].summaries.count_documents({"user_id": payload["user_id"]}) == 1


def test_personal_data_is_redacted_before_storage(client, payload, app_bundle):
    request = {**payload, "pergunta": "Meu CPF é 123.456.789-00; dúvida sobre módulo fotovoltaico"}
    client.post("/chat", json=request)
    stored = app_bundle[1].messages.find_one({"role": "usuario"})["content"]
    assert "123.456.789-00" not in stored
    assert "[CPF OMITIDO]" in stored


def test_observability_has_no_user_or_session(client, payload, app_bundle):
    client.post("/chat", json=payload)
    record = app_bundle[1].observability.find_one()
    assert "user_id" not in record and "session_id" not in record
    assert "question" not in record and "answer" not in record


def test_closing_session_forces_long_term_summary(client, payload, app_bundle):
    client.post("/chat", json=payload)
    response = client.post(f"/sessions/{payload['session_id']}/close", json={"user_id": payload["user_id"]})
    assert response.status_code == 200
    session = app_bundle[1].sessions.find_one({"session_id": payload["session_id"]})
    assert session["status"] == "encerrada"
    assert session["summary"]
    assert app_bundle[1].summaries.count_documents({"session_id": payload["session_id"]}) == 1


def test_other_user_cannot_close_session(client, payload):
    client.post("/chat", json=payload)
    response = client.post(f"/sessions/{payload['session_id']}/close", json={"user_id": "outro-tecnico"})
    assert response.status_code == 403
