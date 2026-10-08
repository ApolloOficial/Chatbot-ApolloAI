# MongoDB e memória

MongoDB é a fonte de verdade das sessões e mensagens; Qdrant armazena os vetores de documentos e resumos. O repository cria índices para:

- `sessions`: índice único `(user_id, session_id)`, estado e contagem de mensagens;
- `messages`: histórico completo, metadados do grafo e TTL de retenção;
- `summaries`: memória de longo prazo formada por resumos recuperáveis de sessões anteriores;
- `observability`: rota, agentes, juiz, latências e contagens, sem campos `user_id` e `session_id`.

O contexto curto usa as últimas mensagens configuradas. A memória longa pesquisa no Qdrant remoto apenas resumos do mesmo `user_id`; MongoDB guarda o registro definitivo. Resumos são gerados em intervalos configuráveis; `POST /sessions/{session_id}/close` força o resumo final e encerra a sessão. Falhas do Qdrant não acionam busca lexical local.

Se MongoDB for obrigatório e estiver indisponível, `/chat` retorna 503 antes de chamar o provedor. Falhas não expõem URI. A sessão de outro usuário retorna 403; uma sessão encerrada retorna 409. A coleção `messages` retém o histórico até o TTL. Versões anteriores também copiavam mensagens em `sessions`; em bases já utilizadas, remova essas cópias com `db.sessions.updateMany({}, {$unset: {messages: ""}})` no MongoDB.

## Docker Compose com Atlas

O `compose.yaml` lê `MONGODB_URI`, `MONGODB_DATABASE` e `MONGODB_TIMEOUT_MS` do arquivo `.env`. Preencha a URI de conexão fornecida pelo Atlas e autorize o IP público da rede em **Network Access** antes de iniciar:

```bash
docker compose up --build
```

Nesse modo, MongoDB, Redis e Qdrant permanecem remotos.
