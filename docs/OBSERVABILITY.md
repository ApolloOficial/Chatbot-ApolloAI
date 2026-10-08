# Observabilidade, custos e ROI

`GET /metrics` expõe formato Prometheus sem `user_id`, `session_id` ou conteúdo das mensagens. São medidos: requisições, turnos por status, erros; latência por agente/modelo, intervalo entre agentes e tempo total; rotas e agentes; bloqueios de entrada e fora de escopo; consultas RAG; rejeições do juiz; falhas MongoDB/MCP; tokens reportados pelo provedor por chamada; custo estimado acumulado e custo por resposta com status sucesso (proxy de resolução). O histograma `apolloai_agent_handoff_seconds` mede do fim de um agente ao início do próximo e inclui preparação de prompt e recuperação RAG quando aplicável. A coleção `observability` no MongoDB registra rota, agentes, quantidade de fontes, decisão do juiz e latência do fluxo, sem campos `user_id` e `session_id`; os agregados de tokens e modelos ficam no Prometheus.

Os callbacks cobrem classificador e todas as chamadas dos agentes, sem estimar tokens pelo tamanho do texto. Chamadas sem metadados e falhas incrementam `apolloai_model_usage_missing_total`; consumo desconhecido não é apresentado como custo comprovadamente zero. A latência exportada do turno fecha em `finally`, incluindo falhas e persistência. Bloqueios são funcionamento esperado do guardrail, separados de erro de serviço. A taxa de erro usa turnos concluídos, não tentativas de autenticação/payload inválido antes do serviço.

A imagem inicia Gunicorn com um diretório multiprocess novo por execução. `/metrics` agrega todos os workers com `MultiProcessCollector`; razões são derivadas dos contadores agregados. O [painel Grafana e as regras](../deploy/monitoring/) usam janelas temporais com SLO p95 ≤ 8 s e erros ≤ 5%. Sem tráfego suficiente, percentis podem ficar sem valor; sem respostas de sucesso, custo por resolução é indefinido. Esses limites são objetivos operacionais configurados nas regras.

Instalação, persistência, acesso por túnel, tracing LangSmith e validação remota estão no [guia de produção](PROMETHEUS_PRODUCTION.md).

## Cenários configuráveis

Use `python scripts/estimate_costs.py`. Para cada cenário de 100 e 1.000 usuários semanais:

- solicitações = usuários × mensagens médias por usuário;
- chamadas de agente = solicitações × agentes médios por solicitação;
- custo = tokens de entrada e saída × preço configurado por milhão;
- resoluções = solicitações × taxa estimada de resolução;
- benefício estimado = resoluções × minutos poupados × custo-hora / 60;
- custo total = custo de IA + parcela semanal da infraestrutura;
- custo por resolução = custo total / resoluções estimadas;
- ROI = (benefício estimado − custo total) / custo total.

Os preços de tokens permanecem em zero porque o cenário padrão usa o plano gratuito da Groq. O custo total inclui a infraestrutura estimada do Learner Lab: US$ 12,80/mês para 100 usuários semanais e US$ 20,40/mês para 1.000 usuários semanais, dentro do orçamento de US$ 50. Esses valores consideram EC2 em `us-east-1`, 8 GB de EBS gp3, um IPv4 público, um segredo no AWS Secrets Manager e pequena reserva para logs; impostos, tráfego excedente e serviços remotos externos não estão incluídos. A imagem fica no GHCR público. Para simular valores diferentes, defina as variáveis opcionais citadas em `app/config.py` no ambiente. Os padrões são 5 mensagens por usuário, 700 tokens de entrada e 350 de saída por chamada, 5 chamadas de modelo por turno técnico (classificador, roteador, especialista, orquestrador e juiz), 1 consulta RAG e 75% de resolução estimada.

O relatório também compara chamadas e tokens diários com `AI_FREE_DAILY_REQUEST_LIMIT` e `AI_FREE_DAILY_TOKEN_LIMIT`. Com as premissas atuais e os limites-base documentados de 1.000 requisições/dia e 200.000 tokens/dia para `openai/gpt-oss-20b`, os dois cenários retornam `free_quota_feasible=false`. Logo, eles servem para estimar custo e demanda, mas a operação integral de 100 ou 1.000 usuários não cabe na cota gratuita sem reduzir mensagens, agentes ou tokens. Confirme sempre os limites exibidos na conta Groq.

Com `TECHNICIAN_HOURLY_COST=0`, o benefício calculado é zero e o ROI exibido é apenas o resultado matemático dessa premissa, **não um ROI observado**. O custo do Neo4j opcional e dos serviços externos também não está incluído no orçamento AWS. Para defender custo por resolução e ROI reais, é preciso registrar resolução confirmada pelo usuário, tempo poupado e custos efetivos.
