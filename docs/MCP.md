# Integração MCP de conhecimento solar

O módulo `app.mcp_server` é um servidor MCP real por transporte `stdio`. Ele publica três ferramentas:

- `buscar_conhecimento_solar`;
- `buscar_procedimento_manutencao`;
- `buscar_orientacao_seguranca`.

O cliente `SolarMCPClient` cria uma sessão MCP, inicializa o protocolo, chama a ferramenta e interpreta o resultado estruturado. O comando e o timeout são configurados por `MCP_SERVER_COMMAND` e `MCP_TIMEOUT_SECONDS`. A indisponibilidade gera `MCPUnavailable`, é contabilizada nas métricas e resulta em resposta controlada; uma função Python local não é apresentada como integração MCP.

Para inspecionar as ferramentas com o Inspector oficial:

```bash
mcp dev app/mcp_server.py
```

Para executar diretamente por stdio:

```bash
python -m app.mcp_server
```

Em testes, o processo real pode ser iniciado pelo cliente. Dublês são usados apenas nos testes unitários do grafo para evitar processos e chamadas pagas.
