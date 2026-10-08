# ☀️ ApolloAI

<p align="center">
  <strong>Assistente multiagente para orientação sobre ativos fotovoltaicos</strong>
</p>

<p align="center">
  <a href="https://github.com/ApolloOficial/Chatbot-ApolloAI/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/ApolloOficial/Chatbot-ApolloAI/actions/workflows/ci.yml/badge.svg"></a>
  <img alt="Python 3.13" src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white">
  <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-Multiagente-1C3C3C">
  <img alt="MongoDB 8" src="https://img.shields.io/badge/MongoDB-8-47A248?logo=mongodb&logoColor=white">
  <img alt="Redis 7" src="https://img.shields.io/badge/Redis-7-DC382D?logo=redis&logoColor=white">
</p>

ApolloAI é uma API Flask que ajuda técnicos de manutenção a consultar informações sobre sistemas fotovoltaicos. Ela combina agentes especializados, busca semântica em fontes técnicas e memória de conversa para produzir respostas rastreáveis.

O chatbot oferece orientação: não aciona equipamentos, registra manutenções nem acessa o banco operacional do aplicativo Apollo.

## Como funciona

- **API:** Flask recebe perguntas do aplicativo Apollo e devolve respostas com fontes.
- **Agentes:** sete papéis construídos com LangChain e coordenados por LangGraph.
- **RAG e segurança:** Qdrant recupera trechos técnicos; guardrails e juiz factual verificam o fluxo.
- **Serviços:** MongoDB mantém sessões e memória, Redis apoia o ranking de rotas, MCP integra ferramentas e A2A expõe a API a agentes externos. Um grafo Neo4j demonstra o extra de BD2.
- **Operação:** métricas Prometheus e implantação em K3s.

```text
Requisição → guardrail de entrada → roteador → especialista → orquestrador
           → juiz factual → guardrail de saída → resposta com fontes
```

Sessões e resumos persistem no MongoDB; as fontes técnicas são indexadas no Qdrant.

Veja o [diagrama completo e as fronteiras dos componentes](docs/ARCHITECTURE.md).

## Início rápido

Requisitos: Python 3.13, acesso a MongoDB, Redis e Qdrant remotos, e uma chave de provedor de IA. O ambiente padrão usa Groq.

```bash
git clone https://github.com/ApolloOficial/Chatbot-ApolloAI.git
cd Chatbot-ApolloAI
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Preencha `.env` com as credenciais e URLs necessárias. Para preparar as fontes do RAG e iniciar a API:

```bash
python -m scripts.convert_pdfs_to_markdown
python -m scripts.index_qdrant
python -m flask --app wsgi run
```

A primeira indexação baixa o modelo local de embeddings e cria as coleções `rag_chunks_v2` e `memoria_resumos_v2`. A API não usa serviços locais como fallback; MongoDB, Redis e Qdrant devem estar acessíveis remotamente.

Após iniciar, consulte `http://localhost:5000/docs` para explorar a API. Variáveis de ambiente e opções de execução estão descritas em [.env.example](.env.example) e no [guia de implantação](docs/DEPLOYMENT.md).

## API

O endpoint principal é `POST /chat`. Quando `AUTH_REQUIRED=true`, envie também `Authorization: Bearer <token-do-serviço>` e `X-User-ID`; o token deve ficar no backend/gateway, nunca no aplicativo mobile.

```http
POST /chat
Content-Type: application/json
Authorization: Bearer <token-do-serviço>
X-User-ID: tecnico-a8f3
```

```json
{
  "user_id": "tecnico-a8f3",
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "pergunta": "Como avaliar degradação em módulos fotovoltaicos?",
  "contexto": {"componente": "módulo fotovoltaico"}
}
```

A resposta inclui `session_id`, `resposta`, `status`, `agentes_chamados` e `fontes` (documento e página), além de campos de segurança quando aplicável.

Outros endpoints: `GET /live`, `GET /health`, `GET /metrics`, `GET /openapi.json` e `GET /docs`. A API também oferece A2A (`/.well-known/agent-card.json`, `/a2a/v1`) e encerramento de sessão (`POST /sessions/{session_id}/close`). O contrato completo está no Swagger UI.

**Extra Neo4j:** após configurar as três credenciais `NEO4J_*` e executar `python -m scripts.seed_neo4j`, consulte `GET /knowledge/impact?componente=Cabo`. A rota percorre sistema, componente, modo de falha e ação; veja [modelo e demonstração](docs/NEO4J.md). O chatbot não depende do Neo4j.

## Testes

```bash
python -m pytest -m "not integration" -q
```

Testes de integração MCP e avaliação do RAG dependem dos serviços remotos e são descritos em [docs/RAG.md](docs/RAG.md) e [docs/MCP.md](docs/MCP.md).

## Documentação

- [Arquitetura](docs/ARCHITECTURE.md) · [Agentes](docs/AGENTS.md) · [RAG e fontes](docs/RAG.md)
- [Guardrails e juiz](docs/GUARDRAILS_AND_JUDGE.md) · [MCP](docs/MCP.md) · [A2A](docs/A2A.md)
- [Implantação](docs/DEPLOYMENT.md) · [AWS Learner Lab](docs/AWS_LEARNER_LAB.md) · [Integração mobile](docs/MOBILE_INTEGRATION.md)
- [Autenticação](docs/AUTHENTICATION.md) · [MongoDB e memória](docs/MONGODB.md) · [Observabilidade](docs/OBSERVABILITY.md)
- [Privacidade](docs/PRIVACY.md) · [Rastreabilidade dos requisitos de IA](docs/REQUIREMENTS_TRACEABILITY.md)
- [Grafo Neo4j e pergunta de negócio](docs/NEO4J.md)
- [Prometheus e Grafana em produção](docs/PROMETHEUS_PRODUCTION.md)
