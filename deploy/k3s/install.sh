#!/usr/bin/env bash
set -euo pipefail

CERT_MANAGER_VERSION="${CERT_MANAGER_VERSION:-v1.21.2}"
INSTALL_SCRIPT="$(mktemp)"
trap 'rm -f -- "$INSTALL_SCRIPT"' EXIT

if ! command -v curl >/dev/null; then
  echo "curl não está instalado." >&2
  exit 1
fi

sudo install -d -m 0755 /etc/rancher/k3s
printf '%s\n' 'secrets-encryption: true' | sudo tee /etc/rancher/k3s/config.yaml >/dev/null

curl --fail --silent --show-error --location https://get.k3s.io --output "$INSTALL_SCRIPT"
sudo sh "$INSTALL_SCRIPT"

mkdir -p "$HOME/.kube"
sudo cp /etc/rancher/k3s/k3s.yaml "$HOME/.kube/config"
sudo chown "$(id -u):$(id -g)" "$HOME/.kube/config"
chmod 600 "$HOME/.kube/config"
export KUBECONFIG="$HOME/.kube/config"

kubectl wait --for=condition=Ready node --all --timeout=180s
for attempt in $(seq 1 90); do
  if kubectl -n kube-system get deployment/traefik >/dev/null 2>&1; then
    break
  fi
  if [[ "$attempt" == "90" ]]; then
    echo "O Deployment do Traefik não foi criado." >&2
    exit 1
  fi
  sleep 2
done
kubectl -n kube-system rollout status deployment/traefik --timeout=180s
kubectl apply -f "https://github.com/cert-manager/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.yaml"
kubectl -n cert-manager rollout status deployment/cert-manager --timeout=300s
kubectl -n cert-manager rollout status deployment/cert-manager-webhook --timeout=300s
kubectl -n cert-manager rollout status deployment/cert-manager-cainjector --timeout=300s

echo "K3s, Traefik e cert-manager ${CERT_MANAGER_VERSION} estão prontos."
