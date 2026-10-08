# Integração com o aplicativo Apollo

## Autenticação e conexão

```text
Aplicativo Apollo → backend autenticado do Apollo → ApolloAI → serviços remotos
```

O backend Apollo valida a sessão do usuário e chama a API por HTTPS com
`Authorization: Bearer` e `X-User-ID`. A identidade do header prevalece sobre
o `user_id` do corpo. O token autentica o serviço chamador e permanece no
backend; o aplicativo não recebe credenciais do ApolloAI, bancos ou provedor de IA.

O ApolloAI valida um token de serviço compartilhado. Não valida diretamente
JWT/OIDC de usuários finais. Rate limiting e limites por usuário pertencem
ao gateway que integra o aplicativo à API.

## Envio de mensagens

```http
POST /chat
Authorization: Bearer <token-do-serviço>
X-User-ID: <identificador-pseudonimizado>
Content-Type: application/json
```

```json
{
  "user_id": "tecnico-001",
  "session_id": "uuid-da-conversa",
  "pergunta": "Quais fatores reduzem a eficiência de um módulo fotovoltaico?",
  "contexto": {
    "componente": "módulo fotovoltaico",
    "fabricante": "opcional",
    "modelo": "opcional",
    "sintoma": "opcional",
    "medicoes": "opcional",
    "condicao_ambiental": "opcional"
  }
}
```

O cliente mantém o mesmo `session_id` durante a conversa e usa um novo
identificador ao iniciar outra sessão. A resposta contém `resposta`, `status`,
`rota`, `agentes_chamados`, `fontes`, `alerta_seguranca` e `motivo_bloqueio`.
As fontes incluem documento, página e URL quando disponíveis. O contrato
completo está em `/openapi.json` e `/docs`.

| Resposta | Tratamento pelo cliente |
|---|---|
| `200` + `sucesso` | Exibir resposta e referências |
| `200` + `bloqueado` | Exibir recusa; não repetir automaticamente |
| `200` + `esclarecimento` | Exibir limitação e solicitar informação adicional |
| `401` | Verificar autenticação e identidade no backend |
| `403` | Impedir acesso à sessão de outra identidade |
| `413` | Reduzir o tamanho do payload |
| `422` | Corrigir os campos indicados na validação |
| `503` | Informar indisponibilidade e permitir nova tentativa controlada |
| `500` | Informar falha interna e registrar o incidente no backend |

A API não implementa chave de idempotência. Repetir uma requisição pode
duplicar mensagens já persistidas; o cliente não deve repetir envios
automaticamente após um timeout. A resposta chega ao término do fluxo,
sem streaming, e o timeout do gateway deve considerar a execução dos agentes.

## Encerramento da sessão

`POST /sessions/{session_id}/close`, com a mesma autenticação e um corpo
`{"user_id": "tecnico-001"}`, gera o resumo final e marca a sessão como
encerrada. O cliente inicia outra conversa com um novo `session_id`.

## Saúde e interface de teste

`/live` verifica se a API responde; `/health` consulta MongoDB, Redis, Qdrant e
MCP. `/metrics` fornece os indicadores ao Prometheus. A configuração do painel
está em [PROMETHEUS_PRODUCTION.md](PROMETHEUS_PRODUCTION.md).

O diretório `frontend` contém uma interface HTML/JS de teste. Ela não envia
o token de serviço e, por isso, não se autentica diretamente na API configurada
para produção. A integração do produto passa pelo backend Apollo.
