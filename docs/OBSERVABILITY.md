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

Os preços de tokens permanecem em zero porque o cenário padrão usa o plano gratuito da Groq. O custo total inclui a infraestrutura estimada do Learner Lab: US$ 12,80/mês para 100 usuários semanais e US$ 20,40/mês para 1.000 usuários semanais, dentro do orçamento de US$ 50. Esses valores consideram EC2 em `us-east-1`, 8 GB de EBS gp3, um IPv4 público, um segredo no AWS Secrets Manager e pequena reserva para logs; impostos, tráfego excedente e serviços remotos externos não estão incluídos. A imagem fica no GHCR público. Para uma simulação diferente, ajuste `AWS_MONTHLY_COST_100_USERS`, `AWS_MONTHLY_COST_1000_USERS`, preços de tokens e `TECHNICIAN_HOURLY_COST`. As demais premissas ficam em `.env.example`: 5 mensagens por usuário, 700 tokens de entrada e 350 de saída por chamada, 4 agentes por solicitação, 1 consulta RAG e 75% de resolução.

O relatório também compara chamadas e tokens diários com `AI_FREE_DAILY_REQUEST_LIMIT` e `AI_FREE_DAILY_TOKEN_LIMIT`. Com as premissas atuais e os limites-base documentados de 1.000 requisições/dia e 200.000 tokens/dia para `openai/gpt-oss-20b`, os dois cenários retornam `free_quota_feasible=false`. Logo, eles servem para estimar custo e demanda, mas a operação integral de 100 ou 1.000 usuários não cabe na cota gratuita sem reduzir mensagens, agentes ou tokens. Confirme sempre os limites exibidos na conta Groq.
