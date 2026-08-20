# Rastreabilidade — disciplina de Inteligência Artificial

| Requisito | Implementação / evidência |
|---|---|
| API Flask com modelo generativo | `app/__init__.py`, `wsgi.py`, `app/llms.py` |
| Cinco ou mais agentes | sete papéis em `app/prompts.py` e `app/llms.py` |
| LangChain e LangGraph | `create_agent` em `app/llms.py`; `StateGraph` em `app/graph.py` |
| Sessões por usuário e memória longa | `app/memory.py`, índices `(user_id, session_id)` e resumos |
| MongoDB em interação conversacional | `ChatService` persiste as duas mensagens e metadados de cada execução |
| Redis | ranking de rotas e fila de indexação degradáveis em `app/services/redis_service.py` |
| MCP | servidor e cliente MCP stdio em `app/mcp_server.py` e `app/services/mcp_client.py`; teste real de handshake, catálogo e busca |
| A2A | Agent Card e JSON-RPC `SendMessage` 1.0 em `app/a2a.py` e `app/routes/a2a.py` |
| RAG com fonte externa | publicação NREL catalogada em `data/solar/fontes.md`; índice em `app/services/rag.py` |
| Juiz de alucinação | nó `juiz_factual` e decisão Pydantic no estado do grafo e MongoDB |
| Guardrails | `app/guardrail.py`, antes do roteador e depois do orquestrador |
| Observabilidade/SRE | Prometheus e coleção Mongo; detalhes em `docs/OBSERVABILITY.md` |
| 100 e 1.000 usuários | `scripts/estimate_costs.py` calcula ambos com premissas configuráveis |
| Latência e índice de erros | histogramas por agente/total, contador e gauge no endpoint `/metrics` |
| Custo, ROI e custo por resolução | `app/services/costs.py`, sem dados empresariais presumidos |
| Arquitetura de alto nível | Mermaid em `docs/ARCHITECTURE.md` |
| Autenticação do cliente | Bearer e identidade confiável `X-User-ID` configuráveis em `app/auth.py` |
| Qualidade do RAG | dataset versionado e gate de hit rate/MRR em `scripts/evaluate_rag.py` |
| CI e code review | `.github/workflows/ci.yml` e `.github/PULL_REQUEST_TEMPLATE.md` |

Os testes automatizados verificam rotas, segurança, RAG, A2A, juiz, memória, falhas, Flask, CORS, WSGI e ausência de FastAPI/PostgreSQL. A CI executa também o transporte MCP real e o stack Docker.
