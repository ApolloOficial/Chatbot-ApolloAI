# Implantação

## Serviços remotos

`docker compose up --build` inicia o ApolloAI somente com MongoDB, Redis e Qdrant remotos definidos no `.env`. O processo recusa URLs locais e configurações sem a chave do Qdrant. `/live` verifica somente o processo Flask/Gunicorn; `/health` verifica MongoDB, Redis, as coleções remotas de RAG e o handshake MCP. Para Claude, configure `AI_PROVIDER=bedrock`, `AI_MODEL`, `AWS_REGION` e uma identidade IAM com `bedrock:InvokeModel`.

## Kubernetes e cloud

`deploy/k8s` fornece uma base independente de provedor com Deployment, Service, ConfigMap, recursos, security context e probes. Antes de aplicar:

1. publique uma imagem imutável e substitua `image` em `deploy/k8s/base/deployment.yaml` ou use a transformação `images` de um overlay;
2. substitua os domínios `.invalid` do ConfigMap por meio de um overlay;
3. crie `apolloai-secrets` usando o secret manager da cloud, tomando `secret.example.yaml` apenas como contrato;
4. forneça MongoDB, Redis e Qdrant remotos e identidade IAM para o Bedrock;
5. configure Ingress/Gateway com TLS;
6. execute `kubectl kustomize deploy/k8s` para revisar o manifesto e, somente no ambiente autorizado, aplique-o.

O arquivo de exemplo de Secret contém apenas marcadores e não faz parte de `kustomization.yaml`. A configuração exige autenticação, MongoDB, Redis, Qdrant e MCP. O deploy real depende da escolha da cloud, registro de imagens, domínio, identidade IAM e credenciais da equipe; nenhum desses estados externos é alegado pelo repositório.

O Deployment usa o ServiceAccount `apolloai`. Associe esse ServiceAccount à função IAM da carga no ambiente AWS. A função deve permitir `bedrock:InvokeModel` para o modelo ou perfil de inferência configurado; não grave chaves AWS estáticas no Secret do Kubernetes.

O overlay pronto para personalização do ambiente de homologação está em `deploy/k8s/overlays/hml`. Consulte o passo a passo em [HOMOLOGATION_KUBERNETES.md](HOMOLOGATION_KUBERNETES.md). Os placeholders impedem uma publicação acidental antes de a equipe definir imagem, domínio e segredos reais.
