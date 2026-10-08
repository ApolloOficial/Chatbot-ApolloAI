# Resumo

<!-- Descreva brevemente o objetivo desta PR. -->

**Card do Jira:** #

## Alterações

<!-- Liste as principais alterações realizadas. -->

-
-
-

## API

<!-- Preencha apenas se aplicável. -->

- Endpoint(s):
- Schema(s) / contrato(s):
- Regra(s) de negócio:

### Camadas alteradas

> Marque os itens alterados substituindo `⬜` por `✅`.

- ⬜ Blueprint / rota
- ⬜ Serviço
- ⬜ Grafo / nó de agente
- ⬜ Prompt / agente LangChain
- ⬜ Guardrail / juiz factual
- ⬜ Schema / validação
- ⬜ OpenAPI / configuração

## Dados e Integrações

> Marque apenas o que foi alterado substituindo `⬜` por `✅`.

- ⬜ MongoDB (sessões, mensagens ou memória)
- ⬜ Redis (ranking de rotas)
- ⬜ Qdrant / RAG / fontes
- ⬜ Neo4j / grafo de conhecimento
- ⬜ MCP
- ⬜ A2A
- ⬜ Autenticação / privacidade
- ⬜ Não se aplica

## Testes

> Marque o que foi validado substituindo `⬜` por `✅`.

- ⬜ Testes unitários
- ⬜ Testes de integração
- ⬜ Avaliação RAG
- ⬜ Teste manual
- ⬜ Cenários de sucesso e erro
- ⬜ Não se aplica

**Comandos executados e resultado:**

```text
<!-- Ex.: python -m pytest -m "not integration" -q -->
```

## Impacto

> Marque os impactos aplicáveis substituindo `⬜` por `✅`.

- ⬜ API / cliente mobile
- ⬜ Dados ou memória
- ⬜ Fontes / índice RAG
- ⬜ Documentação
- ⬜ Infraestrutura / configuração
- ⬜ Não há impacto externo

## Checklist

> Marque os itens concluídos substituindo `⬜` por `✅`.

- ⬜ Código segue a arquitetura Flask e o fluxo de agentes do projeto
- ⬜ Entradas e saídas possuem validação adequada
- ⬜ Sessões e memórias permanecem isoladas por `user_id`
- ⬜ Alterações no RAG preservam fonte e página quando disponíveis
- ⬜ Não há secrets, credenciais ou dados sensíveis versionados
- ⬜ Documentação e métricas atualizadas, quando necessário

## Observações

<!-- Informe pontos de atenção, migrações, reindexação ou dependências desta PR. -->
