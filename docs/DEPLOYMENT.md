# Implantação

## Serviços remotos

`docker compose up --build` inicia o ApolloAI somente com MongoDB, Redis e Qdrant remotos definidos no `.env`. O processo recusa URLs locais e configurações sem a chave do Qdrant. `/live` verifica somente o processo Flask/Gunicorn; `/health` verifica MongoDB, Redis, as coleções remotas de RAG e o handshake MCP. O padrão usa Groq no plano gratuito com `AI_PROVIDER=groq`, `AI_MODEL` e `GROQ_API_KEY`, sem fallback automático.

## AWS Academy Learner Lab

O Learner Lab fornecido à equipe não lista Amazon Bedrock entre os serviços permitidos. Para preservar o orçamento de US$ 50, a implantação recomendada usa uma única instância EC2 com Docker, e não EKS. O procedimento, os limites e a estimativa estão em [AWS_LEARNER_LAB.md](AWS_LEARNER_LAB.md).

## Kubernetes e cloud

`deploy/k8s` fornece uma base independente de provedor com Deployment, Service, ConfigMap, recursos, security context e probes. Antes de aplicar:

1. publique uma imagem imutável e substitua `image` em `deploy/k8s/base/deployment.yaml` ou use a transformação `images` de um overlay;
2. substitua os domínios `.invalid` do ConfigMap por meio de um overlay;
3. crie `apolloai-secrets` usando o secret manager da cloud, tomando `secret.example.yaml` apenas como contrato;
4. forneça MongoDB, Redis e Qdrant remotos e a chave Groq pelo gerenciador de segredos;
5. configure Ingress/Gateway com TLS;
6. execute `kubectl kustomize deploy/k8s` para revisar o manifesto e, somente no ambiente autorizado, aplique-o.

O arquivo de exemplo de Secret contém apenas marcadores e não faz parte de `kustomization.yaml`. A configuração exige autenticação, MongoDB, Redis, Qdrant e MCP. O deploy real depende da escolha da cloud, registro de imagens, domínio, identidade IAM e credenciais da equipe; nenhum desses estados externos é alegado pelo repositório.

O overlay pronto para personalização do ambiente de homologação está em `deploy/k8s/overlays/hml`. Consulte o passo a passo em [HOMOLOGATION_KUBERNETES.md](HOMOLOGATION_KUBERNETES.md). Os placeholders impedem uma publicação acidental antes de a equipe definir imagem, domínio e segredos reais.
