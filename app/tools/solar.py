"""Ferramentas LangChain que consultam o contrato MCP, não funções locais disfarçadas."""

from __future__ import annotations

from langchain.tools import tool

from app.services.mcp_client import SolarMCPClient


def build_solar_tools(client: SolarMCPClient):
    @tool
    def buscar_conhecimento_solar(pergunta: str) -> list[dict]:
        """Recupera trechos técnicos sobre componentes e desempenho fotovoltaico via MCP."""
        return client.search("buscar_conhecimento_solar", pergunta)

    @tool
    def buscar_procedimento_manutencao(pergunta: str) -> list[dict]:
        """Recupera boas práticas de manutenção fotovoltaica via MCP."""
        return client.search("buscar_procedimento_manutencao", pergunta)

    @tool
    def buscar_orientacao_seguranca(pergunta: str) -> list[dict]:
        """Recupera orientação de segurança presente nas fontes via MCP."""
        return client.search("buscar_orientacao_seguranca", pergunta)

    return [buscar_conhecimento_solar, buscar_procedimento_manutencao, buscar_orientacao_seguranca]
