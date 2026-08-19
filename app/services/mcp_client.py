"""Cliente MCP stdio com timeout e degradação explícita."""

from __future__ import annotations

import asyncio
import json
import logging
import shlex
from pathlib import Path
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

logger = logging.getLogger(__name__)


class MCPUnavailable(RuntimeError):
    """Falha controlada na integração MCP."""


class SolarMCPClient:
    def __init__(self, command: str, timeout_seconds: float, cwd: Path | None = None) -> None:
        parts = shlex.split(command, posix=True)
        if not parts:
            raise ValueError("MCP_SERVER_COMMAND não pode ser vazio.")
        self.parameters = StdioServerParameters(
            command=parts[0], args=parts[1:], cwd=str(cwd) if cwd else None,
        )
        self.timeout_seconds = timeout_seconds

    @classmethod
    def from_config(cls, config):
        return cls(config["MCP_SERVER_COMMAND"], config["MCP_TIMEOUT_SECONDS"], Path(config["SOLAR_DATA_DIR"]).parents[1])

    def search(self, tool_name: str, question: str) -> list[dict[str, Any]]:
        try:
            return asyncio.run(asyncio.wait_for(self._search(tool_name, question), timeout=self.timeout_seconds))
        except Exception as error:
            logger.warning("mcp_indisponivel", extra={"error_type": type(error).__name__, "tool": tool_name})
            raise MCPUnavailable("A recuperação técnica está temporariamente indisponível.") from error

    async def _search(self, tool_name: str, question: str) -> list[dict[str, Any]]:
        async with stdio_client(self.parameters) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, {"pergunta": question})
                if result.isError:
                    raise MCPUnavailable("A ferramenta MCP informou uma falha.")
                structured = getattr(result, "structuredContent", None)
                if isinstance(structured, dict):
                    value = structured.get("result", structured)
                    if isinstance(value, list):
                        return value
                for block in result.content:
                    text = getattr(block, "text", None)
                    if text:
                        parsed = json.loads(text)
                        return parsed if isinstance(parsed, list) else parsed.get("result", [])
                return []


class MCPRetriever:
    """Adapta as três ferramentas MCP ao contrato usado pelo LangGraph."""

    TOOLS = {
        "ativos_solares": "buscar_conhecimento_solar",
        "manutencao": "buscar_procedimento_manutencao",
        "seguranca": "buscar_orientacao_seguranca",
    }

    def __init__(self, client: SolarMCPClient) -> None:
        self.client = client

    def retrieve(self, query: str, route: str) -> list[dict[str, Any]]:
        tool = self.TOOLS.get(route, "buscar_conhecimento_solar")
        return self.client.search(tool, query)
