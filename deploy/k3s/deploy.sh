#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CONFIG_FILE="${1:-$ROOT_DIR/deploy/k3s/deploy.env}"
RENDERED="$(mktemp)"
export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/config}"
trap 'rm -f -- "$RENDERED"' EXIT

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Arquivo de configuração não encontrado: $CONFIG_FILE" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$CONFIG_FILE"
set +a

: "${APOLLOAI_IMAGE_TAG:?Configure APOLLOAI_IMAGE_TAG}"
: "${APOLLOAI_HOST:?Configure APOLLOAI_HOST}"
: "${CORS_ORIGINS:?Configure CORS_ORIGINS}"
: "${QDRANT_URL:?Configure QDRANT_URL}"
: "${ACME_EMAIL:?Configure ACME_EMAIL}"
: "${AWS_SECRET_ID:?Configure AWS_SECRET_ID}"
: "${AWS_REGION:?Configure AWS_REGION}"

kubectl apply -f "$ROOT_DIR/deploy/k8s/overlays/hml/namespace.yaml" >/dev/null
bash "$ROOT_DIR/deploy/k3s/sync-secret.sh"

python3 "$ROOT_DIR/deploy/k3s/render.py" \
  --host "$APOLLOAI_HOST" \
  --cors-origin "$CORS_ORIGINS" \
  --qdrant-url "$QDRANT_URL" \
  --image-tag "$APOLLOAI_IMAGE_TAG" \
  --acme-email "$ACME_EMAIL" >"$RENDERED"

kubectl apply -f "$RENDERED"
kubectl -n apolloai-hml wait --for=condition=Ready certificate/apolloai-hml-tls --timeout=5m
kubectl -n apolloai-hml rollout status deployment/apolloai --timeout=5m
kubectl -n apolloai-hml get pods,service,ingress,certificate

echo "Implantação aplicada. Aguarde o certificado e valide https://${APOLLOAI_HOST}/live."
