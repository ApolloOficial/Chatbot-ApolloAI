# MongoDB e memória

MongoDB é o único banco persistente do ApolloAI. O repository cria índices para:

- `sessions`: índice único `(user_id, session_id)` e estado resumido/bounded;
- `messages`: histórico completo, metadados do grafo e TTL de retenção;
- `summaries`: memória de longo prazo formada por resumos recuperáveis de sessões anteriores;
- `observability`: rota, agentes, juiz, latências e contagens sem PII.

O contexto curto usa as últimas mensagens configuradas. A memória longa pesquisa apenas resumos do mesmo `user_id` com termos relevantes à pergunta atual. Resumos são gerados em intervalos configuráveis; `POST /sessions/{session_id}/close` força o resumo final e encerra a sessão. Nenhum dicionário Python ou `MemorySaver` é fonte de verdade.

Se MongoDB for obrigatório e estiver indisponível, `/chat` retorna 503 antes de chamar o provedor. Falhas não expõem URI. A sessão de outro usuário retorna 403. A coleção `messages` retém a cópia completa até o TTL; o array em `sessions` guarda apenas uma janela limitada para impedir crescimento ilimitado.
