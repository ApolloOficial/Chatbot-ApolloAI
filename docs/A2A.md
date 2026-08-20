# Integração A2A

O ApolloAI expõe uma integração entre agentes baseada no Agent2Agent Protocol 1.0. Ela é independente do MCP: A2A permite que outro sistema agêntico descubra e chame o ApolloAI; MCP permite que o ApolloAI consulte as ferramentas de conhecimento solar.

## Descoberta

`GET /.well-known/agent-card.json` publica o Agent Card com:

- interface JSON-RPC e versão de protocolo `1.0`;
- capacidades realmente suportadas, sem anunciar streaming ou push;
- skills de ativos solares, manutenção e segurança;
- esquema Bearer quando `AUTH_REQUIRED=true`;
- cache HTTP e ETag.

Em produção, `PUBLIC_BASE_URL` deve ser uma URL HTTPS pública. O card não contém credenciais nem prompts internos.

## Envio síncrono

`POST /a2a/v1` aceita JSON-RPC 2.0 com o método `SendMessage`. A versão é enviada em `A2A-Version: 1.0`. O adaptador aceita somente partes textuais e converte a mensagem para o mesmo `ChatService` usado por `/chat`, preservando guardrails, juiz, RAG, memória e observabilidade.

```json
{
  "jsonrpc": "2.0",
  "id": "request-001",
  "method": "SendMessage",
  "params": {
    "message": {
      "messageId": "message-001",
      "contextId": "550e8400-e29b-41d4-a716-446655440000",
      "role": "ROLE_USER",
      "parts": [{"text": "Como verificar uma anomalia com segurança?"}],
      "metadata": {"userId": "tecnico-a91f", "contexto": {}}
    }
  }
}
```

Com autenticação habilitada, `metadata.userId` não é confiável e é substituído pelo header `X-User-ID` propagado pelo backend Apollo autenticado.

Operações assíncronas, streaming, push notifications e arquivos não são anunciados nem aceitos nesta versão.
