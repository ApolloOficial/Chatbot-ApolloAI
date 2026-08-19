# Privacidade e retenção

O contrato exige `user_id` pseudonimizado e rejeita e-mail como identificador. Mensagens são sanitizadas antes da persistência para remover CPF, e-mail e padrões comuns de credencial. Logs e métricas não incluem pergunta, resposta, URI, usuário ou sessão.

Sessões são isoladas pelo índice único `(user_id, session_id)`; reutilizar uma sessão de outro usuário retorna HTTP 403. Mensagens recebem `expires_at` e índice TTL, com retenção padrão de 180 dias configurável por `RETENTION_DAYS`. Para atender solicitação de exclusão, o operador do MongoDB deve excluir, dentro do mesmo escopo de `user_id`, documentos das coleções `sessions`, `messages`, `summaries` e `long_term_memories`. Backups precisam seguir a mesma política.
