# Privacidade e retenção

O contrato exige `user_id` pseudonimizado e rejeita e-mail como identificador. O conteúdo das mensagens é sanitizado antes da persistência para remover padrões de CPF, e-mail e credenciais. Essa substituição cobre os padrões definidos em `sanitize_for_storage`; não realiza anonimização geral de texto livre ou dos metadados. As métricas Prometheus não usam perguntas, respostas, usuários ou sessões como labels. O tracing LangSmith é opcional, com ocultação de entradas e saídas configurada por variáveis de ambiente.

As consultas de memória usam a identidade do usuário e a API verifica a propriedade da sessão. O índice único de sessões é `(user_id, session_id)`; uma tentativa de acessar uma sessão atribuída a outra identidade retorna HTTP 403.

A coleção `messages` recebe `expires_at` e índice TTL, com retenção padrão de 180 dias configurável por `RETENTION_DAYS`. Novas mensagens não são copiadas em `sessions`. Bases antigas podem conter cópias embutidas; veja o comando de limpeza em [MONGODB.md](MONGODB.md). O TTL não se aplica aos resumos, aos vetores nem aos registros de observabilidade; novos registros guardam apenas indicadores estruturados, sem texto do juiz. Para limpar texto de registros antigos, execute `db.observability.updateMany({}, {$unset: {"judge_decision.resposta_corrigida": "", "judge_decision.motivos": ""}})` no MongoDB.

A exclusão de dados é operacional: envolve os documentos do usuário nas coleções `sessions`, `messages` e `summaries` do MongoDB e os pontos correspondentes em `memoria_resumos_v2` no Qdrant. O projeto não oferece endpoint de exclusão. Cópias de segurança e traces externos seguem as políticas dos ambientes em que são armazenados.
