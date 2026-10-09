# Autenticação e identidade

As rotas de chat, encerramento de sessão e envio A2A exigem autenticação em execução normal. A application factory aceita `AUTH_REQUIRED=false` em aplicações criadas com `TESTING=true`, usadas nos testes automatizados. Na configuração do serviço:

```dotenv
AUTH_REQUIRED=true
APOLLOAI_API_TOKEN=<segredo forte e exclusivo do serviço>
```

O backend Apollo deve enviar:

```http
Authorization: Bearer <APOLLOAI_API_TOKEN>
X-User-ID: <identificador pseudonimizado obtido da sessão autenticada>
```

Quando esse modo está ativo, o `user_id` do corpo e o `metadata.userId` do A2A são ignorados. Isso impede que o cliente final escolha livremente a identidade usada para acessar o histórico. O token autentica o serviço chamador; autenticação do usuário, rotação do segredo, rate limiting e TLS pertencem ao gateway/backend Apollo.

O segredo nunca deve ser incluído no aplicativo mobile, no frontend local, no Agent Card ou no Git. Em produção, injete-o por secret manager e restrinja a comunicação a HTTPS.

`/live`, `/health`, `/metrics`, `/docs`, `/openapi.json` e o Agent Card não exigem Bearer. O Ingress da API encaminha o prefixo `/`; os serviços de Prometheus e Grafana usam acesso interno separado. A coleta interna não restringe, por si só, o acesso público ao endpoint `/metrics` da API.
