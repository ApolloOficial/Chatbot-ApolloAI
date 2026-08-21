# ☀️ ApolloAI

<p align="center">
  <strong>Inteligência multiagente para orientação segura sobre ativos fotovoltaicos</strong>
</p>

<p align="center">
  <a href="https://github.com/ApolloOficial/Chatbot-ApolloAI/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/ApolloOficial/Chatbot-ApolloAI/actions/workflows/ci.yml/badge.svg"></a>
  <img alt="Python 3.13" src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white">
  <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-Multiagente-1C3C3C">
  <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-8-47A248?logo=mongodb&logoColor=white">
  <img alt="Redis" src="https://img.shields.io/badge/Redis-7-DC382D?logo=redis&logoColor=white">
</p>

<p align="center">
  <a href="#arquitetura">Arquitetura</a> •
  <a href="#configuracao">Configuração</a> •
  <a href="#api">API</a> •
  <a href="#testes">Testes</a> •
  <a href="#documentacao">Documentação</a>
</p>

---

ApolloAI é o módulo de inteligência artificial do Apollo para orientação de Técnicos de Manutenção de ativos fotovoltaicos. A API Flask recebe pergunta e contexto já coletado pelo aplicativo mobile, executa um grafo multiagente e devolve uma resposta fundamentada. Ela não aciona câmera, não lê barcode, não ativa placas, não registra manutenção e não acessa o PostgreSQL operacional do Apollo.

<a id="arquitetura"></a>

## 🧩 Arquitetura

- 🌶️ **API:** Flask com Application Factory, Blueprints, Pydantic, CORS e OpenAPI;
- 🤖 **Multiagentes:** sete papéis criados com LangChain e orquestrados por LangGraph;
- 🛡️ **Fluxo seguro:** `guardrail de entrada → roteador → especialista → juiz factual → orquestrador → guardrail de saída`;
- 📚 **RAG:** índice local persistente, busca híbrida e metadados de fonte;
- 🔌 **Integrações:** MCP para ferramentas e A2A 1.0 para comunicação entre agentes;
- 🍃 **Memória:** MongoDB para sessões, mensagens, resumos e observabilidade;
- ⚡ **Tempo real:** Redis para ranking e fila, sem substituir o histórico persistente;
- 📊 **SRE:** Prometheus, latência, erros, custos estimados e ROI configurável.

O diagrama Mermaid e as fronteiras estão em [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## 🛠️ Requisitos

- Python 3.11 a 3.13 recomendado;
- MongoDB 7 ou 8;
- Redis 7;
- chave Groq ou Google para execução dos agentes em produção.

O ambiente de avaliação usou Python 3.14; os testes passaram, embora o LangChain tenha emitido um aviso de compatibilidade legado do Pydantic nessa versão. A imagem Docker usa Python 3.13.

<a id="configuracao"></a>

## ⚙️ Configuração local

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

No Linux/macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Preencha apenas o provedor escolhido. Nunca versione `.env`. O ApolloAI não usa `DATABASE_URL` nem qualquer credencial PostgreSQL.

Para Groq, o modelo padrão é `openai/gpt-oss-120b`. Se o seu `.env` definir `AI_MODEL`, use um identificador atualmente disponível para a sua conta.

Indexe as fontes:

```bash
python scripts/index_knowledge.py
```

Inicie em desenvolvimento:

```bash
flask --app wsgi run --debug
```

Acesse `http://localhost:5000/docs` para o Swagger UI, `http://localhost:5000/openapi.json` para o contrato e `/` para a interface local de testes. O aplicativo mobile Apollo continua sendo o cliente oficial.

## 🚀 Produção

Em Linux ou no container:

```bash
gunicorn --bind 0.0.0.0:5000 --workers 2 --timeout 90 "wsgi:app"
```

Com MongoDB Atlas, preencha `MONGODB_URI` no `.env` e execute:

```bash
docker compose up --build
```

Nesse modo, o container do ApolloAI acessa o cluster remoto e apenas o Redis é executado localmente. Autorize o IP público da sua rede em **Network Access** no Atlas.

Para executar também o MongoDB localmente, use a configuração complementar:

```bash
docker compose -f compose.yaml -f compose.local.yaml up --build
```

O `compose.local.yaml` substitui a URI do Atlas por `mongodb://mongo:27017` e adiciona o serviço MongoDB. Nenhuma das configurações utiliza PostgreSQL.

<a id="api"></a>

## 🌐 Contrato HTTP

```http
POST /chat
Content-Type: application/json
```

```json
{
  "user_id": "tecnico-a8f3",
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "pergunta": "Qual a diferença entre manutenção preditiva e preventiva?",
  "contexto": {
    "componente": "módulo fotovoltaico",
    "sintoma": "redução de geração observada"
  }
}
```

```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "resposta": "...",
  "status": "sucesso",
  "rota": "manutencao",
  "agentes_chamados": ["roteador", "manutencao", "juiz_factual", "orquestrador"],
  "fontes": [],
  "alerta_seguranca": null,
  "motivo_bloqueio": null
}
```

Outros endpoints:

- `GET /live`: vida do processo, sem depender de serviços externos;
- `GET /health`: prontidão de MongoDB, RAG, MCP e Redis;
- `GET /.well-known/agent-card.json` e `POST /a2a/v1`: descoberta e mensagens A2A 1.0;
- `POST /sessions/{session_id}/close`: encerra a sessão e consolida sua memória longa;
- `GET /metrics`: formato Prometheus, sem PII;
- `GET /openapi.json` e `GET /docs`: documentação da API.

<a id="testes"></a>

## 🧪 Testes

Não são realizadas chamadas pagas nem gravações externas:

```bash
python -m pytest -q -p no:cacheprovider
```

O teste MCP real cria somente o subprocesso local do servidor:

```powershell
$env:RUN_MCP_INTEGRATION="1"
python -m pytest -q -p no:cacheprovider tests/test_mcp_integration.py
```

No Linux/macOS:

```bash
RUN_MCP_INTEGRATION=1 python -m pytest -q -p no:cacheprovider tests/test_mcp_integration.py
```

## 📖 Fonte técnica atual

A fonte oficial consultada é o resumo NREL/FS-7A40-68281. Como o terminal do ambiente de implementação não conseguiu resolver o domínio para baixar o binário, o índice atual usa uma síntese técnica curada e parafraseada, rastreada até a URL oficial. Isso não é apresentado como o PDF original. O pipeline aceita PDFs e preserva número de página quando um PDF real é adicionado. Consulte [data/solar/fontes.md](data/solar/fontes.md) e [docs/RAG.md](docs/RAG.md).

<a id="documentacao"></a>

## 🗂️ Documentação

- 🤖 [Agentes](docs/AGENTS.md)
- 🍃 [MongoDB e memória](docs/MONGODB.md)
- 📚 [RAG e fontes](docs/RAG.md)
- 🛡️ [Guardrails e juiz](docs/GUARDRAILS_AND_JUDGE.md)
- 🔌 [MCP](docs/MCP.md)
- 🤝 [A2A](docs/A2A.md)
- 🔐 [Autenticação](docs/AUTHENTICATION.md)
- 🚀 [Implantação](docs/DEPLOYMENT.md)
- 📊 [Observabilidade, custos e ROI](docs/OBSERVABILITY.md)
- 🔏 [Privacidade e retenção](docs/PRIVACY.md)
- ✅ [Rastreabilidade dos requisitos de IA](docs/REQUIREMENTS_TRACEABILITY.md)

## ⚠️ Limitações reais

- respostas de produção dependem de MongoDB e de um provedor de IA configurado;
- Redis indisponível não apaga o histórico, mas deixa `/health` degradado quando `REDIS_REQUIRED=true`;
- a qualidade do RAG está limitada às fontes efetivamente indexadas;
- a síntese NREL atual é curta e não substitui manuais, normas ou procedimentos internos;
- o Swagger UI carrega seus arquivos visuais de CDN, enquanto `/openapi.json` funciona localmente;
- o custo é estimado por contagem aproximada de tokens; preço e valor de tempo precisam ser configurados;
- ApolloAI não observa o equipamento e não produz diagnóstico confirmado.
