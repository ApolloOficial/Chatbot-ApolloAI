from __future__ import annotations

import json

import pytest

from app.qdrant_store import QdrantUnavailable
from app.services.rag import SolarKnowledgeBase


def test_rag_uses_only_remote_store(workspace_tmp_path):
    class Store:
        configured = True

        def search_document_chunks(self, query, limit):
            assert (query, limit) == ("manutenção preventiva", 5)
            return [{"documento": "fonte.md", "trecho": "Manutenção preventiva."}]

        def is_ready(self):
            return True

    knowledge = SolarKnowledgeBase(workspace_tmp_path, semantic_store=Store())
    assert knowledge.is_ready
    assert knowledge.retrieve("manutenção preventiva")[0]["documento"] == "fonte.md"


def test_rag_does_not_fallback_to_local_document(workspace_tmp_path):
    class Store:
        configured = True

        def search_document_chunks(self, query, limit):
            raise QdrantUnavailable("Qdrant indisponível")

    (workspace_tmp_path / "fonte.md").write_text("Manutenção preventiva.", encoding="utf-8")
    knowledge = SolarKnowledgeBase(workspace_tmp_path, semantic_store=Store())
    with pytest.raises(QdrantUnavailable):
        knowledge.retrieve("manutenção preventiva")


def test_no_source_yields_insufficiency(client, payload):
    response = client.post("/chat", json={**payload, "pergunta": "Assunto inexistente sobre módulo fotovoltaico"})
    assert response.json["status"] == "esclarecimento"
    assert "informações suficientes" in response.json["resposta"]
    assert response.json["fontes"] == []


def test_unsupported_answer_is_rejected_by_judge(client, payload, app_bundle):
    response = client.post("/chat", json={**payload, "pergunta": "Dê uma resposta sem evidência sobre módulo fotovoltaico"})
    assert response.json["status"] == "esclarecimento"
    assert "Não foi possível validar" in response.json["resposta"]
    message = app_bundle[1].messages.find_one({"role": "assistente"})
    assert message["judge_decision"]["decisao"] == "rejeitada"


def test_dangerous_output_is_rejected(client, payload):
    response = client.post("/chat", json={**payload, "pergunta": "Quero uma orientação perigosa sobre segurança e tensão"})
    assert response.json["status"] == "esclarecimento"
    assert "Não foi possível validar" in response.json["resposta"]


def test_hypothesis_is_not_presented_as_diagnosis(client, payload):
    response = client.post("/chat", json=payload)
    assert "hipótese" in response.json["resposta"]
    assert "confirme" in response.json["resposta"]


def test_chat_executes_full_graph(client, payload):
    response = client.post("/chat", json=payload)
    assert response.json["agentes_chamados"] == ["roteador", "ativos_solares", "orquestrador", "juiz_factual"]
    assert response.json["fontes"][0]["documento"].startswith("nrel")


@pytest.mark.parametrize("failed_check", [
    "fundamentada", "segura", "dentro_escopo", "fontes_validas", "hipotese_como_diagnostico",
])
def test_judge_rejects_approval_with_failed_check(client, payload, app_bundle, monkeypatch, failed_check):
    _, memory, runtime, _ = app_bundle
    original_invoke = runtime.invoke

    def invoke(agent_name, content):
        if agent_name == "juiz_factual":
            decision = {
                "decisao": "aprovada", "fundamentada": True, "segura": True,
                "dentro_escopo": True, "fontes_validas": True,
                "hipotese_como_diagnostico": False, "motivos": [], "resposta_corrigida": None,
            }
            decision[failed_check] = False if failed_check != "hipotese_como_diagnostico" else True
            return json.dumps(decision)
        return original_invoke(agent_name, content)

    monkeypatch.setattr(runtime, "invoke", invoke)
    response = client.post("/chat", json=payload)

    assert response.json["status"] == "esclarecimento"
    assert "Não foi possível validar" in response.json["resposta"]
    saved = memory.messages.find_one({"role": "assistente"})
    assert saved["judge_decision"]["decisao"] == "rejeitada"


def test_judge_rejects_correction_without_revised_answer(client, payload, app_bundle, monkeypatch):
    _, memory, runtime, _ = app_bundle
    original_invoke = runtime.invoke

    def invoke(agent_name, content):
        if agent_name == "juiz_factual":
            return json.dumps({
                "decisao": "corrigir", "fundamentada": True, "segura": True,
                "dentro_escopo": True, "fontes_validas": True,
                "hipotese_como_diagnostico": False, "motivos": [], "resposta_corrigida": "  ",
            })
        return original_invoke(agent_name, content)

    monkeypatch.setattr(runtime, "invoke", invoke)
    response = client.post("/chat", json=payload)

    assert response.json["status"] == "esclarecimento"
    saved = memory.messages.find_one({"role": "assistente"})
    assert saved["judge_decision"]["decisao"] == "rejeitada"
    assert "não forneceu uma resposta corrigida" in " ".join(saved["judge_decision"]["motivos"])
