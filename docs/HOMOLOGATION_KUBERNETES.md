# Homologação Kubernetes no AWS Learner Lab

O ambiente de homologação usa K3s em uma única EC2. O overlay
`deploy/k8s/overlays/hml` contém Namespace, Deployment, Service e
ServiceAccount. `deploy/k3s/render.py` acrescenta ConfigMap, ClusterIssuer,
Certificate, TLSStore e Ingress com valores validados no momento do deploy.

## Propriedades do ambiente

- uma réplica para respeitar a memória e o orçamento;
- atualização `Recreate`, evitando duas réplicas simultâneas;
- Traefik como Ingress Controller;
- TLS automático com cert-manager e Let's Encrypt, inclusive no IPv4 público;
- probes `/live` e `/health`;
- execução sem root e sem token Kubernetes montado no Pod;
- segredos obtidos do AWS Secrets Manager pelo perfil da EC2;
- tag de imagem obrigatoriamente vinculada a um commit completo.

## Arquivos operacionais

| Arquivo | Finalidade |
|---|---|
| `deploy/k3s/install.sh` | Instala K3s, Traefik e cert-manager |
| `deploy/k3s/deploy.env.example` | Contrato das configurações públicas |
| `deploy/k3s/sync-secret.sh` | Sincroniza o Secrets Manager com Kubernetes |
| `deploy/k3s/render.py` | Renderiza e valida o manifesto final |
| `deploy/k3s/deploy.sh` | Aplica recursos e acompanha o rollout |
| `deploy/k3s/validate.sh` | Executa homologação remota e captura evidências |

O procedimento completo está em [AWS_LEARNER_LAB.md](AWS_LEARNER_LAB.md).

## Critério de conclusão

- `kubectl get nodes` mostra o nó `Ready`;
- Pod, Service, Ingress e Certificate estão prontos;
- a imagem implantada possui tag `sha-<commit completo>`;
- o manifesto renderizado não contém `.invalid` ou marcadores;
- `/live` e `/health` respondem HTTP 200 via HTTPS;
- `/chat` autenticado retorna fontes;
- A2A, MCP e RAG passam no ambiente remoto;
- métricas e cenários de custo são preservados como evidência;
- nenhuma credencial está no repositório ou na imagem.
