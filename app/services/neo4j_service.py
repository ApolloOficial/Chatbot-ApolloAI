"""Grafo pequeno de conhecimento solar para a demonstração de BD2."""

from __future__ import annotations

SOURCE = "https://www.nrel.gov/docs/fy17osti/68281.pdf"

# Relações curadas a partir da síntese NREL já usada pelo RAG.
PATHS = (
    ("Sistema fotovoltaico", "Cabo", "Dano por animais", "Inspecionar o cabeamento conforme procedimento interno"),
    ("Sistema fotovoltaico", "Cabo", "Esmagamento", "Inspecionar o cabeamento conforme procedimento interno"),
    ("Sistema fotovoltaico", "Inversor", "Desempenho reduzido", "Comparar indicadores e consultar o manual do fabricante"),
    ("Sistema fotovoltaico", "Módulo", "Degradação", "Comparar desempenho, inspecionar e realizar medições autorizadas"),
)

SEED_QUERY = """
MERGE (s:Sistema {nome: $sistema})
MERGE (c:Componente {nome: $componente})
MERGE (f:ModoFalha {nome: $falha})
MERGE (a:AcaoAvaliacao {nome: $acao})
MERGE (s)-[:CONTEM]->(c)
MERGE (c)-[:PODE_APRESENTAR]->(f)
MERGE (f)-[:SUGERE_AVALIAR]->(a)
SET a.fonte = $fonte
"""

# A pergunta de negócio exige percorrer Sistema -> Componente -> ModoFalha -> Ação.
TRAVERSAL_QUERY = """
MATCH (s:Sistema)-[:CONTEM]->(c:Componente)-[:PODE_APRESENTAR]->
      (f:ModoFalha)-[:SUGERE_AVALIAR]->(a:AcaoAvaliacao)
WHERE toLower(c.nome) = toLower($componente)
RETURN s.nome AS sistema, c.nome AS componente, f.nome AS modo_falha,
       a.nome AS acao_avaliacao, a.fonte AS fonte
ORDER BY modo_falha, acao_avaliacao
"""


class Neo4jUnavailable(RuntimeError):
    """Neo4j não foi configurado ou não respondeu."""


class SolarGraph:
    def __init__(self, uri: str | None, user: str | None, password: str | None, database: str = "neo4j", driver=None):
        self.configured = bool(uri and user and password)
        self.database = database
        self.driver = driver
        if driver is None and self.configured:
            try:
                from neo4j import GraphDatabase

                self.driver = GraphDatabase.driver(uri, auth=(user, password))
            except Exception as error:
                raise Neo4jUnavailable("Não foi possível conectar ao Neo4j.") from error

    @classmethod
    def from_config(cls, config):
        return cls(config.get("NEO4J_URI"), config.get("NEO4J_USER"),
                   config.get("NEO4J_PASSWORD"), config.get("NEO4J_DATABASE", "neo4j"))

    def _require_driver(self):
        if not self.driver:
            raise Neo4jUnavailable("Configure NEO4J_URI, NEO4J_USER e NEO4J_PASSWORD.")
        return self.driver

    def seed(self) -> int:
        """Carrega dados demonstrativos sem duplicar nós nem relações."""
        try:
            with self._require_driver().session(database=self.database) as session:
                for system, component, failure, action in PATHS:
                    session.run(SEED_QUERY, sistema=system, componente=component,
                                falha=failure, acao=action, fonte=SOURCE).consume()
        except Neo4jUnavailable:
            raise
        except Exception as error:
            raise Neo4jUnavailable("Não foi possível carregar o grafo.") from error
        return len(PATHS)

    def paths_for_component(self, component: str) -> list[dict]:
        try:
            with self._require_driver().session(database=self.database) as session:
                return [dict(record) for record in session.run(TRAVERSAL_QUERY, componente=component)]
        except Neo4jUnavailable:
            raise
        except Exception as error:
            raise Neo4jUnavailable("Não foi possível consultar o grafo.") from error

    def close(self):
        if self.driver:
            self.driver.close()
