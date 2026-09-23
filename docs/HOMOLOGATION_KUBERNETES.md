# Homologação HTTPS no Kubernetes

O overlay `deploy/k8s/overlays/hml` publica o ApolloAI em um namespace isolado, com duas réplicas, atualização gradual, probes e Ingress HTTPS. Ele pressupõe MongoDB e Redis gerenciados; nenhum banco é criado dentro do cluster.

Este overlay é uma referência para um ambiente Kubernetes já existente. Não crie um cluster EKS dentro do Learner Lab de US$ 50: somente o plano de controle padrão custa cerca de US$ 73 por mês, antes dos nós, volumes e endereços IP. Para o laboratório, siga [AWS_LEARNER_LAB.md](AWS_LEARNER_LAB.md).

## Pré-requisitos

- cluster Kubernetes gerenciado e acesso com `kubectl`;
- Ingress Controller NGINX;
- cert-manager;
- domínio sob controle da equipe;
- imagem publicada em um registry;
- Secret Manager ou outro mecanismo seguro para criar `apolloai-secrets`.
- chave Groq de uma conta mantida no plano gratuito.

Confirme o contexto antes de qualquer alteração:

```powershell
kubectl config current-context
kubectl cluster-info
```

## 1. Personalizar o overlay

Em `deploy/k8s/overlays/hml/kustomization.yaml`, substitua `replace-with-commit-sha`
pela tag imutável `sha-<SHA completo>` publicada pelo workflow de CI. A imagem é
publicada em `ghcr.io/apollooficial/chatbot-apolloai` após os testes de cada push.

Substitua `apolloai-hml.example.com` no `ingress.yaml` e no `configmap-patch.yaml`. Ajuste também `CORS_ORIGINS` para a origem web autorizada. Não use `*` com credenciais.

## 2. Configurar o emissor TLS

Instale o NGINX Ingress Controller e o cert-manager conforme a documentação do provedor. Edite uma cópia local de `deploy/k8s/cluster-issuer.example.yaml`, coloque o e-mail da equipe e aplique:

```powershell
kubectl apply -f caminho/cluster-issuer.yaml
kubectl get clusterissuer letsencrypt-production
```

Não versione a cópia personalizada se ela contiver informações que a equipe não deseja publicar.

## 3. Criar os segredos

O Deployment espera um Secret chamado `apolloai-secrets` no namespace `apolloai-hml`, com estas chaves:

- `APOLLOAI_API_TOKEN`;
- `GROQ_API_KEY`;
- `QDRANT_API_KEY`;
- `MONGODB_URI`;
- `REDIS_URL`.

Use preferencialmente Secret Manager com External Secrets ou Secrets Store CSI. Para um teste inicial, crie um arquivo local `apolloai-hml.secrets.env`, que já é coberto pelo padrão `.env.*` do `.gitignore`:

```dotenv
APOLLOAI_API_TOKEN=troque-por-token-forte
GROQ_API_KEY=troque-pela-chave-groq
QDRANT_API_KEY=troque-pela-chave-do-qdrant
MONGODB_URI=mongodb+srv://...
REDIS_URL=rediss://...
```

Crie primeiro o namespace e depois o Secret:

```powershell
kubectl apply -f deploy/k8s/overlays/hml/namespace.yaml
kubectl -n apolloai-hml create secret generic apolloai-secrets --from-env-file=apolloai-hml.secrets.env
```

O arquivo local de segredos nunca deve ser enviado ao Git. Apague-o com um método apropriado à política da equipe depois de migrar para o Secret Manager.

Se a imagem do GHCR for privada, crie também um Secret do tipo registry e inclua `imagePullSecrets` no Deployment.

## 4. Revisar e aplicar

Renderize o manifesto antes de aplicar:

```powershell
kubectl kustomize deploy/k8s/overlays/hml
kubectl diff -k deploy/k8s/overlays/hml
kubectl apply -k deploy/k8s/overlays/hml
kubectl -n apolloai-hml rollout status deployment/apolloai --timeout=5m
```

## 5. Configurar DNS e validar HTTPS

Obtenha o endereço do Ingress:

```powershell
kubectl -n apolloai-hml get ingress apolloai
```

Crie no DNS um registro `A` ou `CNAME` para o hostname configurado. Depois acompanhe certificado e pods:

```powershell
kubectl -n apolloai-hml get pods,service,ingress,certificate
kubectl -n apolloai-hml describe certificate apolloai-hml-tls
```

Valide os endpoints:

```powershell
curl.exe --fail https://apolloai-hml.example.com/live
curl.exe --fail https://apolloai-hml.example.com/health
```

`/live` verifica o processo. `/health` só retorna `200` quando MongoDB, Redis, RAG e MCP obrigatórios estiverem saudáveis. Autorize no MongoDB Atlas e no Redis apenas o IP de saída/NAT do cluster sempre que possível.

## 6. Critério de conclusão

Marque o bloqueador de homologação como concluído somente quando:

- a imagem implantada estiver vinculada a um commit;
- o certificado for válido e renovável;
- `/live` e `/health` responderem via HTTPS;
- o backend/gateway Apollo concluir uma chamada autenticada a `/chat`;
- nenhuma chave estiver no aplicativo mobile ou no repositório;
- logs e métricas estiverem acessíveis à equipe.
