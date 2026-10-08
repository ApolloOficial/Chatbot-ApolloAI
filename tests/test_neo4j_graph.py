"""O extra de BD2 exige percurso de relações, não busca isolada por nó."""

import os

import pytest

from app.services.neo4j_service import PATHS, SEED_QUERY, TRAVERSAL_QUERY, SolarGraph


class FakeResult:
    def __init__(self, records=()):
        self.records = records

    def __iter__(self):
        return iter(self.records)

    def consume(self):
        return None


class FakeSession:
    def __init__(self):
        self.calls = []

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def run(self, query, **params):
        self.calls.append((query, params))
        return FakeResult([{"sistema": "Sistema fotovoltaico", "componente": "Cabo",
                            "modo_falha": "Esmagamento", "acao_avaliacao": "Inspecionar",
                            "fonte": "https://www.nrel.gov/docs/fy17osti/68281.pdf"}])


class FakeDriver:
    def __init__(self):
        self.sessions = []

    def session(self, database):
        assert database == "neo4j"
        session = FakeSession()
        self.sessions.append(session)
        return session


def test_seed_and_business_traversal():
    driver = FakeDriver()
    graph = SolarGraph(None, None, None, driver=driver)
    assert graph.seed() == len(PATHS)
    assert len(driver.sessions[0].calls) == len(PATHS)
    assert all(query == SEED_QUERY for query, _ in driver.sessions[0].calls)
    assert "MERGE (s)-[:CONTEM]->(c)" in SEED_QUERY
    paths = graph.paths_for_component("Cabo")
    query, params = driver.sessions[1].calls[0]
    assert query == TRAVERSAL_QUERY
    assert params == {"componente": "Cabo"}
    assert all(edge in query for edge in ("[:CONTEM]", "[:PODE_APRESENTAR]", "[:SUGERE_AVALIAR]"))
    assert paths[0]["modo_falha"] == "Esmagamento"


def test_graph_endpoint_auth_and_unavailable(client, app_bundle):
    response = client.get("/knowledge/impact?componente=Cabo")
    assert response.status_code == 503
    app_bundle[0].extensions["apollo_services"]["knowledge_graph"] = SolarGraph(
        None, None, None, driver=FakeDriver(),
    )
    response = client.get("/knowledge/impact?componente=Cabo")
    assert response.status_code == 200
    assert response.json["total"] == 1


@pytest.mark.integration
def test_business_traversal_against_neo4j():
    settings = [os.getenv(name) for name in ("NEO4J_TEST_URI", "NEO4J_TEST_USER", "NEO4J_TEST_PASSWORD")]
    if not all(settings):
        pytest.skip("Configure NEO4J_TEST_URI, NEO4J_TEST_USER e NEO4J_TEST_PASSWORD")
    graph = SolarGraph(*settings)
    try:
        assert graph.seed() == len(PATHS)
        paths = graph.paths_for_component("Cabo")
        assert {item["modo_falha"] for item in paths} >= {"Dano por animais", "Esmagamento"}
        assert all(item["sistema"] == "Sistema fotovoltaico" and item["acao_avaliacao"] for item in paths)
    finally:
        graph.close()
