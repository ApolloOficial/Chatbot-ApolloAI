# Observabilidade, custos e ROI

`GET /metrics` expõe formato Prometheus sem `user_id`, `session_id` ou conteúdo das mensagens. São medidos: requisições, erros e índice de erros; latência por agente e total; rotas e agentes; bloqueios e motivos; consultas RAG; rejeições do juiz; falhas MongoDB/MCP; tokens estimados; custo acumulado e custo por resolução. A coleção `observability` no MongoDB recebe os mesmos metadados de execução sem identificadores pessoais.

## Cenários configuráveis

Use `python scripts/estimate_costs.py`. Para cada cenário de 100 e 1.000 usuários semanais:

- solicitações = usuários × mensagens médias por usuário;
- chamadas de agente = solicitações × agentes médios por solicitação;
- custo = tokens de entrada e saída × preço configurado por milhão;
- resoluções = solicitações × taxa estimada de resolução;
- benefício estimado = resoluções × minutos poupados × custo-hora / 60;
- ROI = (benefício estimado − custo de IA) / custo de IA.

Os padrões de preço e custo-hora são zero, de modo que o projeto não inventa preço de fornecedor nem dado da empresa. Com zero, ROI aparece como `null`. Para uma simulação, preencha explicitamente `PRICE_INPUT_PER_MILLION`, `PRICE_OUTPUT_PER_MILLION` e `TECHNICIAN_HOURLY_COST`. As demais premissas ficam em `.env.example`: 5 mensagens por usuário, 700 tokens de entrada e 350 de saída por chamada, 4 agentes por solicitação, 1 consulta RAG e 75% de resolução. São hipóteses de planejamento, não medições reais.
