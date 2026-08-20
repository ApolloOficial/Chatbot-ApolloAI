from __future__ import annotations

import json

import mongomock
import pytest

from app import create_app
from app.guardrail import normalize
from app.memory import MongoMemoryRepository
from app.services.chat_service import ChatService


class TestMemory(MongoMemoryRepository):
    __test__ = False

    def health(self) -> str:
        self.ensure_indexes()
        return "disponivel"


class FakeRedis:
    def __init__(self):
        self.routes = []

    def record_route(self, route):
        self.routes.append(route)

    def health(self):
        return "indisponivel"


class FakeRagHealth:
    is_ready = True


class FakeMCPHealth:
    def health(self):
        return "disponivel"


class FakeRuntime:
    def __init__(self):
        self.calls = []

    def classify_input(self, message):
        return "APROVADO"

    def invoke(self, name, content):
        self.calls.append((name, content))
        text = normalize(content)
        if name == "roteador":
            if any(term in text for term in ("seguranca", "tensao", "epi", "energiz")):
                route = "seguranca"
            elif any(term in text for term in ("manutenc", "preventiva", "preditiva", "corretiva", "relatorio")):
                route = "manutencao"
            elif any(term in text for term in ("modulo", "placa", "fotovolta", "eficiencia", "inversor", "string")):
                route = "ativos_solares"
            elif any(term in text for term in ("ola", "obrigado", "apolloai")):
                route = "faq_apolloai"
            else:
                route = "fora_escopo"
            return json.dumps({"rota": route, "justificativa": "classificação de teste"})
        if name == "juiz_factual":
            rejected = "pode trabalhar energizado" in text or "especificacao inventada" in text
            return json.dumps({
                "decisao": "rejeitada" if rejected else "aprovada",
                "fundamentada": not rejected, "segura": not rejected, "dentro_escopo": True,
                "fontes_validas": not rejected, "hipotese_como_diagnostico": False,
                "motivos": ["Conteúdo sem evidência ou inseguro."] if rejected else [],
                "resposta_corrigida": None,
            })
        if name == "orquestrador":
            marker = "CONTEÚDO APROVADO PELO JUIZ:\n"
            return content.split(marker, 1)[-1].split("\n\nLIMITAÇÕES:", 1)[0]
        if name == "faq_apolloai":
            return "Olá! Sou o ApolloAI e posso orientar sobre ativos fotovoltaicos, manutenção e segurança."
        if "orientacao perigosa" in text:
            return "Pode trabalhar energizado sem EPI."
        if "sem evidencia" in text:
            return "Especificação inventada: use exatamente 999 V."
        if name == "manutencao":
            return "Preventiva é planejada; preditiva usa tendências; corretiva responde a falhas. São orientações, não registros."
        if name == "seguranca":
            return "Interrompa a intervenção, aplique o procedimento interno de bloqueio e confirme a condição com instrumento apropriado."
        return "A redução pode ter mais de uma causa. Isso é uma hipótese; confirme com inspeção e medições em campo."


class FakeRetriever:
    def __init__(self):
        self.queries = []

    def retrieve(self, query, route):
        self.queries.append((query, route))
        if "assunto inexistente" in normalize(query):
            return []
        return [{
            "documento": "nrel_pv_om_best_practices_sintese.md", "pagina": None,
            "secao": "Manutenção preventiva e corretiva",
            "url": "https://www.nrel.gov/docs/fy17osti/68281.pdf",
            "trecho": "A manutenção preventiva é planejada e a corretiva responde a falhas.", "score": 0.81,
        }]


@pytest.fixture
def app_bundle():
    app = create_app({
        "TESTING": True, "MONGODB_REQUIRED": True,
        "CORS_ORIGINS": ["http://cliente.local"], "SUMMARY_AFTER_MESSAGES": 4,
    })
    memory = TestMemory("mongodb://unused", "apolloai_test", summary_after=4, client=mongomock.MongoClient())
    runtime = FakeRuntime()
    retriever = FakeRetriever()
    redis = FakeRedis()
    service = ChatService(app.config, memory, redis, app.extensions["metrics"], runtime, retriever)
    app.extensions["apollo_services"].update({
        "chat": service, "memory": memory, "rag": FakeRagHealth(), "redis": redis, "mcp": FakeMCPHealth(),
    })
    return app, memory, runtime, retriever


@pytest.fixture
def client(app_bundle):
    return app_bundle[0].test_client()


@pytest.fixture
def payload():
    return {
        "user_id": "tecnico-a91f", "session_id": "550e8400-e29b-41d4-a716-446655440000",
        "pergunta": "Quais fatores podem reduzir a eficiência de um módulo fotovoltaico?", "contexto": {},
    }
