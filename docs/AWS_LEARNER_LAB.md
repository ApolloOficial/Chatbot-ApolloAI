# AWS Academy Learner Lab com K3s

## Decisão de arquitetura

O ApolloAI usa uma única instância EC2 para hospedar um cluster K3s de um nó.
Essa arquitetura comprova containerização e orquestração Kubernetes sem criar um
cluster EKS. O EKS custa US$ 0,10 por hora somente pelo plano de controle, cerca
de US$ 73 por mês, antes da EC2, EBS e IPv4, e ultrapassa o orçamento de US$ 50.

```mermaid
flowchart LR
    Client[Aplicativo ou agente externo] -->|HTTPS| DNS[DNS público]
    DNS --> Traefik[Traefik no K3s]
    Traefik --> API[Pod ApolloAI]
    API --> Groq[Groq Free]
    API --> Mongo[MongoDB remoto]
    API --> Redis[Redis remoto TLS]
    API --> Qdrant[Qdrant Cloud]
    Secrets[AWS Secrets Manager] -->|LabInstanceProfile| Sync[Sincronização na EC2]
    Sync --> KSecret[Kubernetes Secret criptografado]
    KSecret --> API
    GHCR[Imagem pública no GHCR] --> API
```

O K3s utiliza o Traefik incluído na distribuição. O cert-manager solicita e
renova o certificado TLS. O ServiceAccount identifica o Pod apenas dentro do
Kubernetes. O acesso ao Secrets Manager é feito pelo `LabInstanceProfile` da
EC2, sem credenciais AWS permanentes no Pod.

## Estimativa mensal

| Componente | 100 usuários/semana | 1.000 usuários/semana | Premissa |
|---|---:|---:|---|
| EC2 | US$ 7,59 | US$ 15,18 | `t3.micro` ou `t3.small`, 730 h em `us-east-1` |
| IPv4 público | US$ 3,65 | US$ 3,65 | US$ 0,005/h |
| EBS gp3 | US$ 0,64 | US$ 0,64 | 8 GB |
| Secrets Manager | US$ 0,40 | US$ 0,40 | um segredo, sem tráfego relevante |
| Reserva para logs | US$ 0,52 | US$ 0,53 | estimativa de planejamento |
| **Total estimado** | **US$ 12,80** | **US$ 20,40** | abaixo do orçamento de US$ 50 |

O K3s recomenda pelo menos duas CPUs e 2 GB de RAM para um servidor. Uma
`t3.small` está no limite mínimo e deve executar somente uma réplica. Se houver
pressão de memória, redimensione temporariamente para `t3.medium` e acompanhe o
saldo do laboratório. MongoDB, Redis e Qdrant externos não estão incluídos.

Os cenários de uso ultrapassam a referência de 200.000 tokens diários do plano
gratuito configurado. `python scripts/estimate_costs.py` registra essa restrição
com `free_quota_feasible=false`; o orçamento AWS não compra mais cota da Groq.

## 1. Preparar os serviços externos

Confirme antes do deploy:

- MongoDB remoto com URI `mongodb+srv://`;
- Redis remoto com URI `rediss://`;
- Qdrant Cloud com `rag_chunks` e `memoria_resumos` indexadas;
- conta Groq sem forma de pagamento e modelo `openai/gpt-oss-20b` habilitado;
- domínio ou subdomínio controlado pela equipe;
- imagem pública no GHCR com tag `sha-<commit completo>`.

## 2. Configurar a EC2

Use Amazon Linux 2023 `x86_64`, 8 GB de EBS gp3 e o perfil
`LabInstanceProfile`. Libere no Security Group:

- porta 22 somente para o IP da equipe;
- portas 80 e 443 para os clientes;
- nenhuma exposição das portas 5000 e 6443.

Associe um IPv4 estável enquanto o ambiente estiver em uso. Ao excluir a
implantação, libere também a Elastic IP e o volume para interromper a cobrança.

## 3. Criar o segredo

No AWS Secrets Manager, em `us-east-1`, crie `apolloai/hml` como JSON:

```json
{
  "APOLLOAI_API_TOKEN": "valor forte e exclusivo",
  "GROQ_API_KEY": "chave da conta gratuita",
  "QDRANT_API_KEY": "chave do Qdrant Cloud",
  "MONGODB_URI": "mongodb+srv://...",
  "REDIS_URL": "rediss://..."
}
```

O perfil da instância precisa de `secretsmanager:GetSecretValue` apenas para
esse segredo. Confirme na EC2 sem imprimir o conteúdo:

```bash
aws sts get-caller-identity
aws secretsmanager describe-secret --region us-east-1 --secret-id apolloai/hml
```

## 4. Instalar K3s

Na EC2, entre no repositório atualizado e execute:

```bash
git pull --ff-only
bash deploy/k3s/install.sh
kubectl get nodes
```

O script instala K3s, Traefik e cert-manager `v1.21.2`. Os Kubernetes Secrets
são criptografados no armazenamento do K3s. O kubeconfig fica em
`~/.kube/config` com permissão `600`.

## 5. Configurar domínio e deploy

Crie no DNS um registro `A` apontando o domínio para o IPv4 público da EC2.
Depois prepare a configuração sem credenciais:

```bash
cp deploy/k3s/deploy.env.example deploy/k3s/deploy.env
nano deploy/k3s/deploy.env
```

Preencha a tag exata da imagem, domínio, origem CORS, URL do Qdrant, e-mail ACME,
identificador do segredo e região. O arquivo é ignorado pelo Git.

Implante:

```bash
bash deploy/k3s/deploy.sh
```

O deploy sincroniza o Secrets Manager com `apolloai-secrets`, renderiza os
manifestos sem placeholders, aplica uma réplica e espera o rollout. O Pod não
recebe chaves AWS.

## 6. Validar e coletar evidências

Depois que o DNS propagar e o certificado ficar pronto:

```bash
kubectl -n apolloai-hml get pods,service,ingress,certificate
bash deploy/k3s/validate.sh
```

O validador exige HTTP 200 em `/live` e `/health`, chama `/chat` com autenticação,
valida o Agent Card e A2A, executa os testes MCP e RAG contra os serviços remotos
e captura `/metrics`. As evidências ficam em `deploy/k3s/evidence/`, diretório
ignorado pelo Git.

## 7. Operar dentro do orçamento

- pare a EC2 quando o ambiente não estiver sendo demonstrado;
- acompanhe saldo e Cost Explorer;
- não use EKS, NAT Gateway, RDS ou load balancer dedicado;
- mantenha somente uma réplica;
- conserve ao menos US$ 10 para atrasos de contabilização;
- não use **Reset Lab**, pois os recursos podem ser removidos sem restaurar saldo.

Para remover a aplicação sem desinstalar o K3s:

```bash
kubectl delete namespace apolloai-hml
kubectl delete clusterissuer letsencrypt-production
```

Referências: [preço do EKS](https://aws.amazon.com/eks/pricing/),
[requisitos do K3s](https://docs.k3s.io/installation/requirements/),
[instalação do K3s](https://docs.k3s.io/quick-start/) e
[cert-manager](https://cert-manager.io/docs/installation/kubectl/).
