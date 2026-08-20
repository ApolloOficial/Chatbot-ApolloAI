# Autenticação e identidade

O modo local permanece compatível com o cliente de teste usando `AUTH_REQUIRED=false`. Em um ambiente integrado, configure:

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
