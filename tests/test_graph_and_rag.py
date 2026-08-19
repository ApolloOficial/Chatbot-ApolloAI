from __future__ import annotations

from app.config import Config
from app.services.rag import SolarKnowledgeBase


def test_rag_returns_real_source():
    knowledge = SolarKnowledgeBase.from_config(Config.__dict__)
    results = knowledge.retrieve("manutenção preventiva e corretiva")
    assert results
    assert results[0]["url"] == "https://www.nrel.gov/docs/fy17osti/68281.pdf"


def test_rag_returns_empty_for_unrelated_content():
    knowledge = SolarKnowledgeBase.from_config(Config.__dict__)
    assert knowledge.retrieve("receita culinária de bolo de chocolate") == []


def test_no_source_yields_insufficiency(client, payload):
    response = client.post("/chat", json={**payload, "pergunta": "Assunto inexistente sobre módulo fotovoltaico"})
    assert response.json["status"] == "esclarecimento"
    assert "informações suficientes" in response.json["resposta"]
    assert response.json["fontes"] == []


def test_unsupported_answer_is_rejected_by_judge(client, payload, app_bundle):
    response = client.post("/chat", json={**payload, "pergunta": "Dê uma resposta sem evidência sobre módulo fotovoltaico"})
    assert "informações suficientes" in response.json["resposta"]
    message = app_bundle[1].messages.find_one({"role": "assistente"})
    assert message["judge_decision"]["decisao"] == "rejeitada"


def test_dangerous_output_is_rejected(client, payload):
    response = client.post("/chat", json={**payload, "pergunta": "Quero uma orientação perigosa sobre segurança e tensão"})
    assert "informações suficientes" in response.json["resposta"] or "não é possível" in response.json["resposta"].lower()


def test_hypothesis_is_not_presented_as_diagnosis(client, payload):
    response = client.post("/chat", json=payload)
    assert "hipótese" in response.json["resposta"]
    assert "confirme" in response.json["resposta"]


def test_chat_executes_full_graph(client, payload):
    response = client.post("/chat", json=payload)
    assert response.json["agentes_chamados"] == ["roteador", "ativos_solares", "juiz_factual", "orquestrador"]
    assert response.json["fontes"][0]["documento"].startswith("nrel")
