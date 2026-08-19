"""Servidor MCP real de conhecimento solar, executável por transporte stdio."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from app.config import Config
from app.services.rag import SolarKnowledgeBase

mcp = FastMCP("apolloai-solar-knowledge", instructions="Recupera somente trechos indexados e seus metadados.")
knowledge = SolarKnowledgeBase.from_config(Config.__dict__)


@mcp.tool()
def buscar_conhecimento_solar(pergunta: str) -> list[dict]:
    """Busca informações sobre componentes, desempenho e ambiente fotovoltaico."""
    return knowledge.retrieve(pergunta, "ativos_solares")


@mcp.tool()
def buscar_procedimento_manutencao(pergunta: str) -> list[dict]:
    """Busca boas práticas de manutenção fotovoltaica presentes nas fontes."""
    return knowledge.retrieve(pergunta, "manutencao")


@mcp.tool()
def buscar_orientacao_seguranca(pergunta: str) -> list[dict]:
    """Busca orientação de segurança presente nas fontes técnicas."""
    return knowledge.retrieve(pergunta, "seguranca")


if __name__ == "__main__":
    mcp.run(transport="stdio")
