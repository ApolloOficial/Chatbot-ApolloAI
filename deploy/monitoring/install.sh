#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/config}"
NAMESPACE="apolloai-hml"
kubectl -n "$NAMESPACE" get deployment apolloai >/dev/null
kubectl get storageclass local-path >/dev/null
if ! kubectl -n "$NAMESPACE" get secret grafana-admin >/dev/null 2>&1; then
  PASSWORD_FILE="$(mktemp)"
  trap 'rm -f -- "$PASSWORD_FILE"' EXIT
  chmod 600 "$PASSWORD_FILE"
  read -r -s -p "Senha inicial do Grafana (mínimo 16 caracteres): " grafana_password
  printf '\n'
  if [[ ${#grafana_password} -lt 16 ]]; then
    echo "A senha deve ter pelo menos 16 caracteres." >&2
    exit 1
  fi
  printf '%s' "$grafana_password" >"$PASSWORD_FILE"
  unset grafana_password
  kubectl -n "$NAMESPACE" create secret generic grafana-admin --from-file=password="$PASSWORD_FILE" >/dev/null
fi
kubectl apply -k "$ROOT_DIR/deploy/monitoring"
kubectl -n "$NAMESPACE" rollout status deployment/prometheus --timeout=180s
kubectl -n "$NAMESPACE" rollout status deployment/grafana --timeout=180s
kubectl -n "$NAMESPACE" exec deployment/prometheus -- promtool check config /etc/prometheus/prometheus.yml
echo "Monitoramento instalado. Use port-forward e túnel para acessar o Grafana."
