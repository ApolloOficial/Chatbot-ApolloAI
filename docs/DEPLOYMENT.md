# Implantação

## Stack local

`docker compose up --build` inicia ApolloAI, MongoDB e Redis. `/live` verifica somente o processo Flask/Gunicorn; `/health` verifica MongoDB, Redis, RAG e o handshake MCP real.

## Kubernetes e cloud

`deploy/k8s` fornece uma base independente de provedor com Deployment, Service, ConfigMap, recursos, security context e probes. Antes de aplicar:

1. publique uma imagem imutável e substitua `image` em `deployment.yaml`;
2. substitua os domínios `.invalid` do ConfigMap;
3. crie `apolloai-secrets` usando o secret manager da cloud, tomando `secret.example.yaml` apenas como contrato;
4. use MongoDB e Redis gerenciados ou forneça serviços equivalentes;
5. configure Ingress/Gateway com TLS;
6. execute `kubectl kustomize deploy/k8s` para revisar o manifesto e, somente no ambiente autorizado, aplique-o.

O arquivo de exemplo de Secret contém apenas marcadores e não faz parte de `kustomization.yaml`. A configuração exige autenticação, MongoDB, Redis e MCP. O deploy real depende da escolha da cloud, registro de imagens, domínio e credenciais da equipe; nenhum desses estados externos é alegado pelo repositório.
