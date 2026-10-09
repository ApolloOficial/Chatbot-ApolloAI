# Funcionalidades e implementação

| Funcionalidade | Implementação |
|---|---|
| API Flask com modelo generativo | `app/__init__.py`, `wsgi.py`, `app/llms.py` |
| Cinco ou mais agentes | seis papéis em `app/prompts.py` e `app/llms.py` |
| LangChain e LangGraph | `create_agent` em `app/llms.py`; `StateGraph` em `app/graph.py` |
| Sessões por usuário e memória longa | `app/memory.py`, índices `(user_id, session_id)` e resumos |
| Persistência conversacional | `ChatService` grava mensagens e metadados; falhas de dependência retornam erro controlado |
| Redis | serviço remoto obrigatório e ranking de rotas em `app/services/redis_service.py` |
| Neo4j (extra BD2) | entidades e traversal em `app/services/neo4j_service.py`, rota `GET /knowledge/impact`, carga `scripts/seed_neo4j.py`; demonstração em `docs/NEO4J.md` |
| MCP | servidor e cliente MCP stdio em `app/mcp_server.py` e `app/services/mcp_client.py`; teste real de handshake, catálogo e busca |
| A2A | Agent Card e JSON-RPC `SendMessage` 1.0 em `app/a2a.py` e `app/routes/a2a.py` |
| RAG com fonte externa | NREL e 19 PDFs IEA PVPS catalogados em `data/solar/fontes.md`; busca no Qdrant remoto em `app/services/rag.py` |
| Juiz de alucinação | nó `juiz_factual` e decisão Pydantic no estado do grafo e MongoDB |
| Guardrails | `app/guardrail.py`, na entrada e após a decisão do juiz |
| Observabilidade/SRE | Prometheus e coleção Mongo; detalhes em `docs/OBSERVABILITY.md` |
| 100 e 1.000 usuários | `scripts/estimate_costs.py` calcula ambos com premissas configuráveis |
| Latência e índice de erros | histogramas por agente, intervalo entre agentes e total; contadores e razão de erros em `/metrics` |
| Custo, ROI e custo por resolução | `app/services/costs.py`, sem dados empresariais presumidos |
| Arquitetura de alto nível | Mermaid em `docs/ARCHITECTURE.md` |
| Autenticação do cliente | Bearer e identidade confiável `X-User-ID` configuráveis em `app/auth.py` |
| Qualidade do RAG | dataset versionado e gate de hit rate/MRR em `scripts/evaluate_rag.py` |
| Integração contínua e template de PR | `.github/workflows/ci.yml` e `.github/PULL_REQUEST_TEMPLATE.md` |
| Cloud, container e orquestração | K3s em EC2, manifestos em `deploy/k8s` e automação em `deploy/k3s` |
| Credenciais fora do Git | `.gitignore`, AWS Secrets Manager e gate `scripts/check_tracked_secrets.py` na CI |

Os testes automatizados verificam rotas, segurança, RAG, A2A, juiz, memória, falhas, traversal Neo4j e contratos Flask. A CI executa testes isolados e constrói a imagem; testes MCP, Neo4j remoto e avaliação RAG real exigem serviços externos e não são parte da suíte isolada.
