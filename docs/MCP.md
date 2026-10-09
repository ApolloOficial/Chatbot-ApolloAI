# Integração MCP de conhecimento solar

O módulo `app.mcp_server` usa o SDK MCP v1 (`FastMCP`) por transporte `stdio`. Ele publica três ferramentas:

- `buscar_conhecimento_solar`;
- `buscar_procedimento_manutencao`;
- `buscar_orientacao_seguranca`.

O cliente `SolarMCPClient` cria uma sessão MCP, inicializa o protocolo, chama a ferramenta e interpreta o resultado estruturado. O ApolloAI calcula o embedding da consulta no processo Flask e envia o vetor junto com a pergunta; chamadas MCP diretas podem omitir o vetor e o servidor o calcula localmente. Assim, o fluxo HTTP não carrega o modelo no subprocesso MCP a cada busca. O comando e o timeout são configurados por `MCP_SERVER_COMMAND` e `MCP_TIMEOUT_SECONDS`. A indisponibilidade gera `MCPUnavailable`, é contabilizada nas métricas e resulta em resposta controlada; uma função Python local não é apresentada como integração MCP.

Para inspecionar as ferramentas com o Inspector oficial:

```bash
mcp dev app/mcp_server.py
```

Para executar diretamente por stdio:

```bash
python -m app.mcp_server
```

Em testes, o processo real pode ser iniciado pelo cliente. Dublês são usados apenas nos testes unitários do grafo para evitar processos e chamadas pagas.

## Configuração de clientes externos

No Python do ambiente do projeto (3.13, com dependências e `.env` configurados):

```bash
python scripts/print_mcp_config.py
```

Copie o JSON gerado para `.cursor/mcp.json`, ou para a configuração de servidores
MCP do Cline. Os caminhos absolutos apontam para o Python que executou o script
e para o servidor deste checkout; não contêm credenciais. O servidor pode ser
iniciado fora da pasta do projeto e lê o `.env` pela localização do código.
As três ferramentas são anotadas como leitura. Isso informa intenção ao
cliente, mas não substitui controle de acesso às fontes.

No modo Agent do Cursor e no Cline, consultar o catálogo e solicitar uma busca
de manutenção preventiva fotovoltaica. O resultado inclui o documento e a
página quando disponíveis.
Não é necessário ter Flask/Gunicorn no ar para essa demonstração; o Qdrant
remoto deve estar indexado e acessível. Logs do servidor não devem usar stdout,
reservado ao protocolo.
