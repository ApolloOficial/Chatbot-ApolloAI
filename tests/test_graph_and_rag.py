from __future__ import annotations

import json

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


def test_rag_retrieves_iea_pdf_from_portuguese_query():
    knowledge = SolarKnowledgeBase.from_config(Config.__dict__)
    results = knowledge.retrieve("Como avaliar degradação e modos de falha em módulos fotovoltaicos?")

    assert results
    assert results[0]["documento"] == "IEA-PVPS-T13-30-2025-REPORT-Degradation-and-Failure.pdf"
    assert results[0]["pagina"] is not None


def test_rag_persists_sparse_embeddings(tmp_path):
    documents = tmp_path / "documentos"
    documents.mkdir()
    (documents / "fonte.md").write_text(
        "Photovoltaic module degradation and failure modes support preventive maintenance.",
        encoding="utf-8",
    )
    index_path = tmp_path / "indice.json"
    knowledge = SolarKnowledgeBase(documents, index_path)

    assert knowledge.index_all() == 1
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    embedding = payload["chunks"][0]["embedding"]

    assert payload["version"] == 3
    assert payload["embedding"] == "signed_feature_hashing_sparse_v1"
    assert len(embedding) < knowledge.dimensions // 10


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
