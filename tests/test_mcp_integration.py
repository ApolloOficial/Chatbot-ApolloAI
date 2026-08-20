from __future__ import annotations

import os

import pytest

from app.config import Config
from app.services.mcp_client import SolarMCPClient


@pytest.mark.integration
@pytest.mark.skipif(os.getenv("RUN_MCP_INTEGRATION") != "1", reason="requer criação de subprocesso MCP local")
def test_real_stdio_mcp_contract_returns_indexed_source():
    client = SolarMCPClient.from_config(Config.__dict__)
    results = client.search("buscar_procedimento_manutencao", "manutenção preventiva e corretiva")
    assert results
    assert results[0]["documento"] == "nrel_pv_om_best_practices_sintese.md"


@pytest.mark.integration
@pytest.mark.skipif(os.getenv("RUN_MCP_INTEGRATION") != "1", reason="requer criação de subprocesso MCP local")
def test_real_stdio_mcp_health_checks_required_tools():
    client = SolarMCPClient.from_config(Config.__dict__)
    assert client.health(cache_seconds=0) == "disponivel"
