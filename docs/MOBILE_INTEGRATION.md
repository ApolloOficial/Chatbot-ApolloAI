# Checklist de integração com o aplicativo mobile

## Topologia recomendada

```text
Aplicativo Apollo → backend/gateway autenticado do Apollo → ApolloAI → MongoDB / Redis / Qdrant remotos / Groq
```

O aplicativo não deve conter `APOLLOAI_API_TOKEN`, credenciais de banco ou chaves do provedor de IA. O backend/gateway valida a sessão do usuário, gera uma identidade pseudonimizada e chama o ApolloAI por HTTPS com `Authorization: Bearer` e `X-User-ID`.

## O que já está pronto

- ✅ `POST /chat` com validação Pydantic e contexto tipado do ativo;
- ✅ `POST /sessions/{session_id}/close` para resumo final e encerramento;
- ✅ respostas estruturadas com status, rota, fontes, página e alertas;
- ✅ isolamento de sessões por identidade e bloqueio de acesso cruzado;
- ✅ autenticação serviço-a-serviço configurável;
- ✅ memória persistente no MongoDB e suporte Redis remoto;
- ✅ RAG com fontes NREL/IEA PVPS, guardrails e juiz factual;
- ✅ OpenAPI, Swagger UI, `/live`, `/health` e métricas Prometheus;
- ✅ Docker, base Kubernetes e testes automatizados de API, RAG, MCP e A2A.

## Bloqueadores para integração em homologação

### P0 — obrigatórios

- [ ] **Definir o caminho de autenticação.** Confirmar que o mobile chamará o backend Apollo, e não o ApolloAI diretamente. Se a chamada direta for obrigatória, substituir o segredo estático atual por validação de JWT/OIDC antes da integração.
- [ ] **Publicar um ambiente de homologação HTTPS.** Escolher cluster/provedor, publicar imagem imutável, configurar IPv4 ou hostname público, certificado, Ingress/Gateway e Secret Manager.
- [ ] **Deixar `/health` saudável no ambiente implantado.** Validar MongoDB Atlas, Redis Cloud, RAG e MCP a partir da rede do cluster. A conexão TLS do Atlas ainda precisa ser confirmada fora da rede local atual.
- [ ] **Configurar segredos de homologação.** Definir token exclusivo, chave do Qdrant, URIs gerenciadas e `GROQ_API_KEY` de uma conta mantida no plano gratuito.
- [ ] **Congelar ou versionar o contrato.** O endpoint atual é `/chat`; decidir se a integração será mantida assim ou publicada como `/v1/chat` antes de distribuir o app.
- [ ] **Definir idempotência.** Retries de rede do mobile podem duplicar mensagens. Adicionar uma chave de requisição/idempotência ou definir uma política explícita antes de habilitar retry automático.
- [ ] **Executar teste ponta a ponta com o mobile.** Validar autenticação, criação e retomada de `session_id`, envio de contexto, exibição de fontes, encerramento de sessão e todos os códigos HTTP.

## Contrato que o cliente precisa implementar

O backend chamador envia:

```http
POST /chat
Authorization: Bearer <token-do-serviço>
X-User-ID: <identificador-pseudonimizado>
Content-Type: application/json
```

```json
{
  "user_id": "identidade-substituida-pelo-header",
  "session_id": "uuid-da-conversa",
  "pergunta": "Mensagem do técnico",
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

O cliente deve tratar:

| HTTP | Comportamento esperado |
|---|---|
| `200` + `sucesso` | Exibir resposta e referências |
| `200` + `bloqueado` | Exibir recusa segura sem retry automático |
| `200` + `esclarecimento` | Exibir limitação e solicitar informação adicional |
| `401` | Renovar autenticação no backend; nunca embutir token fixo no app |
| `403` | Descartar a sessão local incompatível e impedir acesso cruzado |
| `422` | Corrigir o payload; não repetir sem alteração |
| `503` | Mostrar indisponibilidade e permitir retry controlado |

## Validações antes de produção

- [ ] medir latência p50/p95 e definir timeout do cliente/gateway compatível com o fluxo multiagente;
- [ ] executar carga para a quantidade prevista de usuários e configurar réplicas/HPA;
- [ ] implementar rate limiting, limite por usuário e proteção contra abuso no gateway;
- [ ] criar dashboards e alertas para erro, latência, MongoDB, Redis, MCP e provedor de IA;
- [ ] validar política de retenção, pseudonimização, consentimento e exclusão de dados;
- [ ] confirmar backup/restauração do MongoDB e estratégia de recuperação;
- [ ] validar UX em rede lenta, perda de conexão e retomada da conversa;
- [ ] revisar exibição de alertas de segurança e links das fontes no mobile;
- [ ] executar teste de segurança e revisar permissões do ambiente;
- [ ] obter aceite funcional dos técnicos e registrar critérios de go-live.

## Definição de pronto

A integração está pronta quando um build de homologação do mobile consegue conversar por HTTPS sem possuir segredos do ApolloAI, manter isolamento e continuidade de sessão, apresentar fontes e alertas, recuperar-se dos erros definidos e passar o teste ponta a ponta com `/health` saudável no ambiente implantado.
