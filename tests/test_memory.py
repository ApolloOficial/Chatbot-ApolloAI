from __future__ import annotations

import mongomock

from app import create_app
from app.memory import MemoryUnavailable, MongoMemoryRepository


class FakeSemanticStore:
    configured = True

    def __init__(self):
        self.indexed = []

    def upsert_summary(self, user_id, session_id, summary, created_at):
        self.indexed.append({"user_id": user_id, "session_id": session_id, "resumo": summary, "created_at": created_at})

    def search_summaries(self, user_id, query, limit):
        return [item | {"score": 0.91} for item in self.indexed if item["user_id"] == user_id][:limit]


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


def test_observability_discards_judge_text(app_bundle):
    memory = app_bundle[1]
    memory.save_observation({"judge_decision": {
        "decisao": "corrigir", "resposta_corrigida": "contato@example.com",
        "motivos": ["CPF 123.456.789-00"],
    }})
    record = memory.observability.find_one()
    assert record["judge_decision"] == {"decisao": "corrigir"}
    assert "contato@example.com" not in str(record)


def test_closed_session_rejects_new_turn(client, payload, app_bundle):
    assert client.post("/chat", json=payload).status_code == 200
    assert client.post(f"/sessions/{payload['session_id']}/close", json={"user_id": payload["user_id"]}).status_code == 200
    response = client.post("/chat", json=payload)
    assert response.status_code == 409
    assert app_bundle[1].messages.count_documents({"session_id": payload["session_id"]}) == 2


def test_messages_are_not_copied_into_sessions(client, payload, app_bundle):
    client.post("/chat", json=payload)
    session = app_bundle[1].sessions.find_one({"session_id": payload["session_id"]})
    assert "messages" not in session
    assert session["message_count"] == 2


def test_late_enrichment_failure_does_not_duplicate_turn(client, payload, app_bundle, monkeypatch):
    memory = app_bundle[1]
    assert client.post("/chat", json=payload).status_code == 200

    def unavailable(*_args):
        raise RuntimeError("offline")

    monkeypatch.setattr(memory.semantic_store, "upsert_summary", unavailable)
    monkeypatch.setattr(memory, "save_observation", lambda *_: (_ for _ in ()).throw(MemoryUnavailable()))
    response = client.post("/chat", json={**payload, "pergunta": "Obrigado ApolloAI"})
    assert response.status_code == 200
    assert memory.messages.count_documents({"session_id": payload["session_id"]}) == 4


def test_test_frontend_is_not_served_in_production():
    app = create_app({
        "PUBLIC_BASE_URL": "https://apollo.example.com",
        "QDRANT_URL": "https://qdrant.example.com",
        "MONGODB_URI": "mongodb+srv://mongo.example.com",
        "REDIS_URL": "rediss://redis.example.com",
        "CORS_ORIGINS": ["https://apollo.example.com"],
        "QDRANT_API_KEY": "test", "APOLLOAI_API_TOKEN": "test",
        "AI_MODEL": "test-model", "AI_PROVIDER": "groq", "GROQ_API_KEY": "test",
    })
    assert app.test_client().get("/").status_code == 404


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


def test_summary_is_indexed_and_recovered_semantically():
    semantic = FakeSemanticStore()
    memory = MongoMemoryRepository(
        "mongodb://unused", "semantic_test", summary_after=2,
        client=mongomock.MongoClient(), semantic_store=semantic,
    )
    memory.start_session("tecnico-1", "sessao-anterior")
    memory.save_message("tecnico-1", "sessao-anterior", "usuario", "Quero planejar uma viagem para Salvador")
    memory.save_message("tecnico-1", "sessao-anterior", "assistente", "Posso ajudar a organizar os dados")
    memory.maybe_summarize("tecnico-1", "sessao-anterior")

    assert semantic.indexed and semantic.indexed[0]["session_id"] == "sessao-anterior"
    _, memories = memory.context("tecnico-1", "sessao-atual", "Quero viajar nas férias")
    assert memories[0]["summary"] == semantic.indexed[0]["resumo"]
    assert memories[0]["score"] == 0.91
