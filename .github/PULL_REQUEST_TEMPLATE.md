# Resumo

<!-- Explique o objetivo desta PR e o resultado esperado. -->

**Issue/Tarefa:** #

## Alterações

<!-- Liste as principais alterações implementadas. -->

-
-
-

## API e agentes

<!-- Preencha somente o que se aplicar. -->

- Endpoint(s), contrato(s) ou schema(s):
- Blueprints, serviço(s) ou grafo(s) alterado(s):
- Agente(s), guardrail(s), prompt(s) ou tool(s) afetado(s):

## Dados e integrações

> Marque os itens alterados substituindo `- [ ]` por `- [x]`.

- [ ] MongoDB (sessões, mensagens, resumos ou índices)
- [ ] Redis
- [ ] Qdrant / RAG / documentos indexados
- [ ] MCP ou A2A
- [ ] Autenticação, privacidade ou retenção de dados
- [ ] Configuração de ambiente (`.env.example`)
- [ ] OpenAPI ou documentação técnica
- [ ] Não se aplica

## Validação

> Indique os comandos executados e os resultados relevantes.

- [ ] `python -m pytest`
- [ ] Testes de integração
- [ ] Teste manual da API ou interface
- [ ] Cenários de sucesso, falha e autorização verificados
- [ ] Não se aplica

**Comandos e resultado:**

```text
# Ex.: python -m pytest -q
```

## Impacto e riscos

- Impacto para usuário, API ou operação:
- Migração, reindexação ou configuração necessária:
- Plano de reversão, se aplicável:

## Checklist

- [ ] A mudança respeita a arquitetura Flask, serviços e grafo de agentes do projeto.
- [ ] Entradas e saídas continuam validadas pelos schemas e guardrails aplicáveis.
- [ ] O acesso a sessões e memórias permanece isolado por `user_id`.
- [ ] Não há segredos, credenciais, PII ou dados de produção versionados.
- [ ] Métricas, logs e documentação foram atualizados quando necessário.
- [ ] Alterações em RAG preservam fonte, documento e página quando disponíveis.

## Observações para revisão

<!-- Informe dependências, limitações conhecidas ou pontos que merecem atenção. -->