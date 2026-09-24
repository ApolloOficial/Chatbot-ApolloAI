# Implantação

## AWS Learner Lab

A implantação oficial usa K3s em uma única EC2. Essa escolha fornece Kubernetes
e mantém o orçamento abaixo de US$ 50 sem o custo fixo do EKS. Consulte
[AWS_LEARNER_LAB.md](AWS_LEARNER_LAB.md).

O fluxo é:

1. a CI testa o código e os manifestos;
2. a CI publica uma imagem imutável `sha-<commit completo>` no GHCR;
3. a EC2 executa K3s com Traefik;
4. o `LabInstanceProfile` lê um segredo no AWS Secrets Manager;
5. o script cria `apolloai-secrets` sem expor valores;
6. o renderizador injeta apenas configurações públicas no manifesto;
7. cert-manager emite o certificado HTTPS;
8. a homologação remota coleta saúde, chat, A2A, MCP, RAG e métricas.

## Serviços obrigatoriamente remotos

- MongoDB com `mongodb+srv://`;
- Redis com `rediss://`;
- Qdrant com HTTPS e chave de API;
- Groq no plano gratuito, sem fallback de provedor.

O processo recusa URLs locais, ausência de autenticação e dependências
obrigatórias desabilitadas. `/live` verifica o processo; `/health` retorna 200
somente quando MongoDB, Redis, Qdrant e MCP estão disponíveis.

## Kubernetes

`deploy/k8s/base` contém recursos independentes do ambiente. O overlay de
homologação reduz o consumo para um único nó K3s. ConfigMap, Ingress e emissor
TLS são gerados por `deploy/k3s/render.py`, que valida domínio, HTTPS, e-mail e
tag da imagem antes de produzir YAML.

O Secret não possui arquivo de exemplo com valores substituíveis. Seu contrato
é definido por estas chaves no AWS Secrets Manager:

- `APOLLOAI_API_TOKEN`;
- `GROQ_API_KEY`;
- `QDRANT_API_KEY`;
- `MONGODB_URI`;
- `REDIS_URL`.

O ServiceAccount não recebe IAM Role. Em K3s, o host EC2 usa o
`LabInstanceProfile` somente durante a sincronização do segredo.
