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

ApolloAI é o módulo de inteligência artificial do Apollo para orientação de Técnicos de Manutenção de ativos fotovoltaicos. A API Flask foi projetada para receber perguntas e o contexto coletado pelo aplicativo mobile, executar um grafo multiagente e devolver uma resposta fundamentada. Ela não aciona câmera, não lê barcode, não ativa placas, não registra manutenção e não acessa o PostgreSQL operacional do Apollo.

<a id="arquitetura"></a>

## 🧩 Arquitetura

- 🌶️ **API:** Flask com Application Factory, Blueprints, Pydantic, CORS e OpenAPI;
- 🤖 **Multiagentes:** sete papéis criados com LangChain e orquestrados por LangGraph;
- 🛡️ **Fluxo seguro:** `guardrail de entrada → roteador → especialista → juiz factual → orquestrador → guardrail de saída`;
- 📚 **RAG:** Qdrant remoto obrigatório, vetores calculados sem API de embeddings e metadados de fonte;
- 🔌 **Integrações:** MCP para ferramentas e A2A 1.0 para comunicação entre agentes;
- 🍃 **Memória:** MongoDB para sessões, mensagens, resumos e observabilidade;
- ⚡ **Tempo real:** Redis para ranking de rotas, sem substituir o histórico persistente;
- 📊 **SRE:** Prometheus, latência, erros, custos estimados e ROI configurável.

O runtime opera sem fallback de provedor, rota, banco ou índice. Configuração local de MongoDB, Redis ou Qdrant é rejeitada no startup; indisponibilidade desses serviços ou saída inválida do classificador e do roteador encerra a requisição com erro controlado.

O diagrama Mermaid e as fronteiras estão em [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## 🛠️ Requisitos

- Python 3.11 a 3.13 recomendado;
- MongoDB 7 ou 8 remoto;
- Redis 7 remoto com TLS;
- Qdrant remoto com URL HTTPS e chave de API;
- conta Groq no plano gratuito e chave de API; a AWS Academy hospeda somente a aplicação.

O ambiente de avaliação usou Python 3.14; os testes passaram, embora o LangChain tenha emitido um aviso de compatibilidade legado do Pydantic nessa versão. A imagem Docker usa Python 3.13.

<a id="configuracao"></a>

## ⚙️ Configuração

### Qdrant: chunks e memória semântica

Configure `QDRANT_URL` com uma URL HTTPS remota e `QDRANT_API_KEY`. Converta os PDFs com `python -m scripts.convert_pdfs_to_markdown` e execute `python -m scripts.index_qdrant`. O indexador lê os Markdown atuais, exige uma conversão para cada PDF e cria as coleções `rag_chunks` e `memoria_resumos` caso não existam. Os vetores são calculados por hashing no processo de indexação e enviados ao Qdrant, sem chamadas à API de embeddings. A busca exige o Qdrant remoto; se ele estiver indisponível, a API retorna erro em vez de consultar arquivos ou um índice local. A similaridade por hashing tem limitações semânticas. Os resumos de sessões são indexados em `memoria_resumos`; MongoDB continua sendo a fonte de verdade.

Para uma indexação limpa, exclua previamente `rag_chunks` e `memoria_resumos` no Qdrant remoto. O indexador recusa coleções não vazias e não apaga dados remotos; após uma execução interrompida, exclua as coleções antes de tentar novamente.

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

Configure `PUBLIC_BASE_URL` com HTTPS, as URIs remotas do MongoDB e Redis, `QDRANT_URL`, `QDRANT_API_KEY` e `APOLLOAI_API_TOKEN`. URLs de `localhost` e Redis sem TLS são recusados fora dos testes. Nunca versione `.env`. O ApolloAI não usa `DATABASE_URL` nem credenciais PostgreSQL.

O ambiente padrão usa `AI_PROVIDER=groq` e `AI_MODEL=openai/gpt-oss-20b`. Mantenha a conta Groq no plano gratuito e configure `GROQ_API_KEY`; ao atingir a cota, a API falha de forma controlada, sem trocar automaticamente de provedor. Gemini permanece selecionável por configuração. Os vetores do RAG são calculados localmente e não consomem a cota de nenhum modelo generativo.

Indexe as fontes no Qdrant remoto:

```bash
python -m scripts.index_qdrant
```

Para validar o processo Flask com todas as dependências remotas configuradas:

```bash
python -m flask --app wsgi run
```

Durante essa validação, acesse `http://localhost:5000/docs` para o Swagger UI, `http://localhost:5000/openapi.json` para o contrato e `/` para a interface de testes. O processo pode ser iniciado em uma máquina de desenvolvimento, mas recusa MongoDB, Redis e Qdrant locais. O aplicativo mobile Apollo é o cliente previsto para a integração oficial.

## 🚀 Produção

O ambiente oficial usa K3s em uma única EC2 do AWS Learner Lab. A CI publica a
imagem com uma tag imutável vinculada ao commit; o K3s executa o Pod atrás do
Traefik e o cert-manager mantém o HTTPS.

```bash
bash deploy/k3s/install.sh
cp deploy/k3s/deploy.env.example deploy/k3s/deploy.env
nano deploy/k3s/deploy.env
bash deploy/k3s/deploy.sh
```

As credenciais são lidas do AWS Secrets Manager pelo `LabInstanceProfile` da
EC2 e sincronizadas com um Kubernetes Secret. Nenhuma chave AWS é entregue ao
Pod. Depois da propagação do DNS e da emissão do certificado, execute:

```bash
bash deploy/k3s/validate.sh
```

O procedimento completo está em
[docs/AWS_LEARNER_LAB.md](docs/AWS_LEARNER_LAB.md). MongoDB, Redis e Qdrant
permanecem remotos. Não há pilha local de bancos, índice local ou troca
automática de provedor.

<a id="api"></a>

## 🌐 Contrato HTTP

```http
POST /chat
Authorization: Bearer <token-do-serviço>
X-User-ID: tecnico-a8f3
Content-Type: application/json
```

Os headers de autenticação são obrigatórios quando `AUTH_REQUIRED=true`. O token pertence ao backend/gateway Apollo e nunca deve ser incluído no aplicativo mobile.

```json
{
  "user_id": "tecnico-a8f3",
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "pergunta": "Como avaliar degradação e modos de falha em módulos fotovoltaicos?",
  "contexto": {
    "componente": "módulo fotovoltaico",
    "sintoma": "degradação de desempenho observada"
  }
}
```

```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "resposta": "...",
  "status": "sucesso",
  "rota": "ativos_solares",
  "agentes_chamados": ["roteador", "ativos_solares", "juiz_factual", "orquestrador"],
  "fontes": [
    {
      "documento": "IEA-PVPS-T13-30-2025-REPORT-Degradation-and-Failure.pdf",
      "pagina": 10,
      "url": "https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-systems/"
    }
  ],
  "alerta_seguranca": null,
  "motivo_bloqueio": null
}
```

Outros endpoints:

- `GET /live`: vida do processo, sem depender de serviços externos;
- `GET /health`: prontidão de MongoDB, coleções do Qdrant remoto, MCP e Redis;
- `GET /.well-known/agent-card.json` e `POST /a2a/v1`: descoberta e mensagens A2A 1.0;
- `POST /sessions/{session_id}/close`: encerra a sessão e consolida sua memória longa;
- `GET /metrics`: formato Prometheus, sem PII;
- `GET /openapi.json` e `GET /docs`: documentação da API.

<a id="testes"></a>

## 🧪 Testes

Os testes unitários usam serviços simulados e não fazem chamadas pagas:

```bash
python -m pytest -m "not integration" -q -p no:cacheprovider
```

O teste de integração MCP cria um subprocesso e consulta o Qdrant remoto configurado:

```powershell
$env:RUN_MCP_INTEGRATION="1"
python -m pytest -q -p no:cacheprovider tests/test_mcp_integration.py
```

No Linux/macOS:

```bash
RUN_MCP_INTEGRATION=1 python -m pytest -q -p no:cacheprovider tests/test_mcp_integration.py
```

A avaliação completa do RAG também exige coleções remotas indexadas:

```bash
RUN_RAG_EVALUATION=1 python -m pytest -m integration -q tests/test_rag_evaluation.py
```

## 📖 Fontes técnicas atuais

O corpus reúne a síntese curada NREL/FS-7A40-68281 e 19 PDFs originais da IEA PVPS sobre desempenho, manutenção, degradação, falhas, clima, agrivoltaicos, sistemas flutuantes, PV+BESS, sustentabilidade e ciclo de vida. O pipeline preserva documento e página e aceita consultas técnicas em português sobre as fontes em inglês. Consulte [data/solar/fontes.md](data/solar/fontes.md) e [docs/RAG.md](docs/RAG.md).

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
- ☁️ [AWS Academy Learner Lab](docs/AWS_LEARNER_LAB.md)
- 📱 [Integração com o aplicativo mobile](docs/MOBILE_INTEGRATION.md)
- 📊 [Observabilidade, custos e ROI](docs/OBSERVABILITY.md)
- 🔏 [Privacidade e retenção](docs/PRIVACY.md)
- ✅ [Rastreabilidade dos requisitos de IA](docs/REQUIREMENTS_TRACEABILITY.md)

## 🛡️ Princípios de operação

O ApolloAI foi projetado para apoiar decisões técnicas com segurança, rastreabilidade e responsabilidade operacional:

- **Respostas fundamentadas:** orientações técnicas são vinculadas às fontes recuperadas pelo RAG, com documento e página;
- **Decisão assistida:** o chatbot organiza evidências e próximos passos, preservando a autoridade de manuais, normas, medições e procedimentos internos;
- **Memória confiável:** MongoDB mantém sessões e histórico persistente, enquanto Redis oferece recursos complementares de baixa latência;
- **Segurança por padrão:** guardrails, juiz factual, identidade pseudonimizada e isolamento de sessões protegem o fluxo conversacional;
- **Operação observável:** endpoints de saúde, métricas Prometheus e registros estruturados permitem acompanhar dependências, latência, erros e custos estimados;
- **Integração controlada:** a arquitetura recomendada usa autenticação serviço-a-serviço e HTTPS para manter credenciais fora do aplicativo mobile.

Os critérios de homologação, implantação e go-live estão documentados no [checklist de integração mobile](docs/MOBILE_INTEGRATION.md).
