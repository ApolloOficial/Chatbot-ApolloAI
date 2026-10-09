"""Servidor MCP stdio com ferramentas de consulta à base solar no Qdrant."""

from __future__ import annotations

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from app.config import Config
from app.services.rag import SolarKnowledgeBase

mcp = FastMCP("apolloai-solar-knowledge", instructions="Recupera somente trechos indexados e seus metadados.")
knowledge = SolarKnowledgeBase.from_config(Config.__dict__)


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def buscar_conhecimento_solar(pergunta: str, vetor_consulta: list[float] | None = None) -> list[dict]:
    """Busca informações sobre componentes, desempenho e ambiente fotovoltaico."""
    return knowledge.retrieve(pergunta, "ativos_solares", vetor_consulta)


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def buscar_procedimento_manutencao(pergunta: str, vetor_consulta: list[float] | None = None) -> list[dict]:
    """Busca boas práticas de manutenção fotovoltaica presentes nas fontes."""
    return knowledge.retrieve(pergunta, "manutencao", vetor_consulta)


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
def buscar_orientacao_seguranca(pergunta: str, vetor_consulta: list[float] | None = None) -> list[dict]:
    """Busca orientação de segurança presente nas fontes técnicas."""
    return knowledge.retrieve(pergunta, "seguranca", vetor_consulta)


if __name__ == "__main__":
    mcp.run(transport="stdio")
