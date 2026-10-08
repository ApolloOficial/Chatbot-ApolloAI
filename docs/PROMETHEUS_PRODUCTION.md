# Prometheus e Grafana na EC2 do AWS Academy

Os arquivos de `deploy/monitoring` configuram Prometheus, Grafana, coleta de
métricas e armazenamento persistente no namespace `apolloai-hml`. Os comandos
de instalação são executados no terminal da EC2; o acesso às páginas usa um
túnel entre o computador da equipe e a instância.

## Confirmar a instalação existente

```bash
hostname
free -h
df -h
command -v kubectl || true
sudo systemctl is-active k3s || true
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}'
sudo ss -ltnp
```

Verificar qual processo serve o chatbot hoje, a imagem/commit e as portas
ocupadas antes de instalar K3s ou migrar o serviço. Se já houver K3s, reutilizar
o cluster e conferir `kubectl get nodes` e `kubectl get pods -A`. Se o cluster
usar outro namespace, adaptar o namespace do Kustomize e a descoberta de pods;
o exemplo acompanha `apolloai-hml` dos arquivos existentes.

Para uma EC2 sem cluster, consulte
[AWS_LEARNER_LAB.md](AWS_LEARNER_LAB.md), seções 3 a 6: preparar serviços
remotos/segredos, `bash deploy/k3s/install.sh`, configurar `deploy.env` e
`bash deploy/k3s/deploy.sh`. A imagem deve corresponder ao commit selecionado no deploy.
O script de instalação escreve a configuração do K3s; não executá-lo novamente
sobre um cluster com configuração própria sem revisar o arquivo existente.

Prometheus/Grafana acrescentam requests de 100m CPU e 256 MiB RAM, limites
combinados de 600m CPU/768 MiB RAM e PVCs de 3 GiB. Isso se soma ao chatbot,
embeddings, K3s e cert-manager. Validar capacidade real antes de subir a pilha;
as estimativas financeiras precisam considerar esse consumo de recursos.
O PVC `local-path` persiste em reinícios de pods, mas não protege contra perda
do nó/volume, exclusão de PVC/namespace ou reset do laboratório.

## Instalar a coleta e o painel

Com a imagem ApolloAI em execução e dentro da pasta do repositório:

```bash
kubectl -n apolloai-hml get deployment apolloai
kubectl get storageclass local-path
bash deploy/monitoring/install.sh
kubectl -n apolloai-hml get pods,pvc,service
```

O instalador pede a senha inicial do Grafana sem ecoá-la, cria o Secret
`grafana-admin` somente se ainda não existir e aplica o Kustomize. O login é
`admin`; a senha não é impressa nem escrita no repositório. Alterar o Secret
posteriormente não redefine a senha de um usuário já salvo no banco Grafana;
usar a interface autenticada ou o procedimento de reset da versão instalada.

O Prometheus descobre cada pod `app=apolloai` na porta nomeada `http`, usando
permissão apenas para ler pods no namespace. Isso evita coletar por um Service
que alternaria as réplicas. Dentro de cada pod, o cliente Python agrega os dois
workers do Gunicorn. O diretório multiprocess é criado antes dos imports, e o
hook `child_exit` remove gauges de workers encerrados, conforme a
[documentação do cliente Python](https://prometheus.github.io/client_python/multiprocess/).

Retenção: até 15 dias e aproximadamente 1 GB de blocos, o primeiro limite
atingido prevalece; WAL/head exigem espaço adicional. O PVC tem 2 GiB.
Grafana provisiona automaticamente a fonte e o dashboard `ApolloAI - SRE e modelos`.
Reaplicar o Kustomize atualiza ConfigMaps com hash e provoca rollout quando
os arquivos mudam. Não há Alertmanager: regras aparecem em Alerts do
Prometheus, sem envio automático de e-mail/mensagens.

## Acesso aos painéis

Os Services são internos (`ClusterIP`), sem Ingress, NodePort ou portas públicas
3000/9090. Em dois terminais da EC2:

```bash
kubectl -n apolloai-hml port-forward --address 127.0.0.1 service/grafana 3000:3000
```

```bash
kubectl -n apolloai-hml port-forward --address 127.0.0.1 service/prometheus 9090:9090
```

Esses endereços pertencem à EC2, não ao navegador do seu notebook. Para acesso
pelo notebook com SSH autorizado, abra um túnel no terminal local:

```bash
ssh -i CAMINHO_DA_CHAVE -L 3000:127.0.0.1:3000 -L 9090:127.0.0.1:9090 ec2-user@IP_ATUAL
```

Então abra `http://localhost:3000/d/apolloai-sre` e `http://localhost:9090` no
notebook. Se o acesso disponível for exclusivamente pelo console, usar um
túnel Session Manager quando habilitado pela conta, ou estabelecer o acesso
SSH autorizado. Não abrir as portas dos painéis para `0.0.0.0/0` para resolver
a diferença entre localhost da EC2 e do notebook.

## Validar com tráfego real

```bash
kubectl -n apolloai-hml exec deployment/prometheus -- promtool check config /etc/prometheus/prometheus.yml
kubectl -n apolloai-hml exec deployment/prometheus -- promtool check rules /etc/prometheus/rules.yml
curl --fail --silent http://127.0.0.1:9090/api/v1/targets
curl --fail --silent --get http://127.0.0.1:9090/api/v1/query --data-urlencode 'query=up{job="apolloai"}'
```

No console do Prometheus, `up{job="apolloai"}` deve ser 1 para cada pod em
execução. No chat autenticado, enviar uma pergunta técnica, uma injeção
bloqueada e uma pergunta que passe pelo modelo. Aguardar duas ou três coletas.
Conferir aumento de turnos, bloqueios, latência, chamadas e tokens. Um bloqueio
não incrementa `apolloai_turns_total{status="erro"}`. Dublês dos testes unitários
não têm tokens do provedor; isso não é evidência de consumo em produção.

Para falhas, usar homologação ou os testes isolados, sem desligar serviços
compartilhados. Falha de provedor/Redis/Mongo/MCP deve aparecer como `erro`, com
latência observada. Regras de latência/erro exigem ao menos 20 turnos na janela
de 5 minutos e persistência de 5 minutos, para evitar alertas por uma amostra
isolada. O painel usa p95 em janela, interpolado pelos buckets do histograma.

Consultas úteis:

```promql
# p95 e erro dos objetivos operacionais (8 s / 5%)
apolloai:sli_latency_p95:5m
apolloai:sli_error_ratio:5m

# tokens informados por modelo e direção no período
sum by (modelo, direcao) (increase(apolloai_model_tokens_total[1h]))

# custo estimado IA por resposta de sucesso; sem sucesso, resultado indefinido
sum(increase(apolloai_estimated_cost_total[1h])) / sum(increase(apolloai_resolutions_total[1h]))
```

Para verificar persistência após coletar dados, reiniciar somente o Deployment
Prometheus com `kubectl -n apolloai-hml rollout restart deployment/prometheus`,
aguardar rollout e consultar o intervalo anterior. Guardar prints do painel,
Targets, regras e resultados em `deploy/k3s/evidence/`, sem segredos. O
[validador existente](../deploy/k3s/validate.sh) valida chat, A2A, MCP e RAG.

## Preços e cenários de uso

`PRICE_INPUT_PER_MILLION` e `PRICE_OUTPUT_PER_MILLION` são preços do modelo
configurado, na mesma moeda. Em `.env`/Compose eles são propagados à API. No
K3s, ajustar o ConfigMap e reiniciar o Deployment da API para aplicar:

```bash
kubectl -n apolloai-hml edit configmap apolloai-config
kubectl -n apolloai-hml rollout restart deployment/apolloai
```

Valores zero representam a premissa de plano gratuito, não ausência de tokens.
O custo usa tokens reportados em cada chamada, incluindo classificador e
agentes. `apolloai_model_usage_missing_total` sinaliza ausência de metadados
ou chamadas com falha, cujo consumo não é conhecido. Não substitui a fatura.
A contagem de `sucesso` é um proxy técnico de resolução, incluindo respostas
sociais; não prova que o técnico solucionou o problema no equipamento.

```bash
python -m scripts.estimate_costs
```

O estimador cobre 100 e 1.000 usuários/semana, demanda/cotas, IA,
infraestrutura, custo por resolução e ROI baseado em premissas. Informar
minutos poupados e custo-hora reais; sem benefício conhecido, não alegar ROI
positivo. O custo do painel mostra IA; custo total/ROI são do estimador.

## Tracing com LangSmith

Adicionar opcionalmente `LANGSMITH_API_KEY` ao JSON do Secrets Manager usado
pelo projeto. O sincronizador permite essa chave sem torná-la obrigatória.
No ConfigMap, definir `LANGSMITH_TRACING=true`,
`LANGSMITH_PROJECT=apolloai-interdisciplinar` e manter
`LANGSMITH_HIDE_INPUTS=true`/`LANGSMITH_HIDE_OUTPUTS=true`. Executar o deploy
para sincronizar o Secret e reiniciar a API. Em Compose, as mesmas variáveis
ficam no `.env`, conforme o exemplo versionado.

LangChain/LangGraph emitem os traces automaticamente. Abrir o projeto no
LangSmith após uma pergunta sintética e conferir nós/modelo/tokens/duração.
Os flags de ocultação seguem a
[documentação de privacidade do LangSmith](https://docs.langchain.com/langsmith/mask-inputs-outputs).
Não enviar conversas reais para demonstrar o trace nem registrar chaves em
prints. Com `LANGSMITH_TRACING=false`, a API mantém somente as métricas locais
e os registros no MongoDB.

## Execução com Docker Compose

Para executar a API e o monitoramento com Docker Compose, configure os
serviços remotos e execute:

```bash
docker compose -f compose.yaml -f compose.monitoring.yaml config --quiet
docker compose -f compose.yaml -f compose.monitoring.yaml up -d --build
```

Definir `GRAFANA_ADMIN_PASSWORD` no `.env` antes. Prometheus coleta
`apolloai:5000` nessa rede Docker. Os serviços usam os volumes e configurações
definidos em `compose.monitoring.yaml`.
Não executar sobre outra implantação com portas já ocupadas sem conferir a
configuração.
