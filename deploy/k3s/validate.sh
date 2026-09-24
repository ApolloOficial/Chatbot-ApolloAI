#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CONFIG_FILE="${1:-$ROOT_DIR/deploy/k3s/deploy.env}"
if [[ -f "$CONFIG_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$CONFIG_FILE"
  set +a
fi

: "${APOLLOAI_DOMAIN:?Configure APOLLOAI_DOMAIN}"
BASE_URL="https://${APOLLOAI_DOMAIN}"
NAMESPACE="${APOLLOAI_NAMESPACE:-apolloai-hml}"
EVIDENCE_DIR="${EVIDENCE_DIR:-$ROOT_DIR/deploy/k3s/evidence}"
mkdir -p "$EVIDENCE_DIR"

TOKEN="$(kubectl -n "$NAMESPACE" get secret apolloai-secrets -o jsonpath='{.data.APOLLOAI_API_TOKEN}' | base64 --decode)"
USER_ID="validacao-remota"
SESSION_ID="$(python3 -c 'import uuid; print(uuid.uuid4())')"
MESSAGE_ID="$(python3 -c 'import uuid; print(uuid.uuid4())')"
HEADER_FILE="$(mktemp)"
trap 'rm -f -- "$HEADER_FILE"' EXIT
chmod 600 "$HEADER_FILE"
printf 'Authorization: Bearer %s\nX-User-ID: %s\n' "$TOKEN" "$USER_ID" >"$HEADER_FILE"

curl --fail --silent --show-error "$BASE_URL/live" | tee "$EVIDENCE_DIR/live.json"
curl --fail --silent --show-error "$BASE_URL/health" | tee "$EVIDENCE_DIR/health.json"
curl --fail --silent --show-error "$BASE_URL/.well-known/agent-card.json" | tee "$EVIDENCE_DIR/agent-card.json"

curl --fail --silent --show-error \
  --request POST "$BASE_URL/chat" \
  --header @"$HEADER_FILE" \
  --header "Content-Type: application/json" \
  --data "{\"user_id\":\"$USER_ID\",\"session_id\":\"$SESSION_ID\",\"pergunta\":\"Quais fatores causam degradação em módulos fotovoltaicos?\",\"contexto\":{}}" \
  | tee "$EVIDENCE_DIR/chat.json"

curl --fail --silent --show-error \
  --request POST "$BASE_URL/a2a/v1" \
  --header @"$HEADER_FILE" \
  --header "A2A-Version: 1.0" \
  --header "Content-Type: application/json" \
  --data "{\"jsonrpc\":\"2.0\",\"id\":\"remote-smoke\",\"method\":\"SendMessage\",\"params\":{\"message\":{\"messageId\":\"$MESSAGE_ID\",\"contextId\":\"$SESSION_ID-a2a\",\"role\":\"ROLE_USER\",\"parts\":[{\"text\":\"Como avaliar a degradação de módulos fotovoltaicos?\"}]}}}" \
  | tee "$EVIDENCE_DIR/a2a.json"

curl --fail --silent --show-error "$BASE_URL/metrics" >"$EVIDENCE_DIR/metrics.prom"
kubectl -n "$NAMESPACE" get pods,service,ingress,certificate -o wide >"$EVIDENCE_DIR/kubernetes.txt"
kubectl -n "$NAMESPACE" exec deployment/apolloai -- \
  env RUN_MCP_INTEGRATION=1 python -m pytest -q -p no:cacheprovider tests/test_mcp_integration.py \
  | tee "$EVIDENCE_DIR/mcp.txt"
kubectl -n "$NAMESPACE" exec deployment/apolloai -- \
  env RUN_RAG_EVALUATION=1 python -m pytest -q -p no:cacheprovider tests/test_rag_evaluation.py \
  | tee "$EVIDENCE_DIR/rag.txt"

python3 - "$EVIDENCE_DIR" <<'PY'
import json
import pathlib
import sys

directory = pathlib.Path(sys.argv[1])
live = json.loads((directory / "live.json").read_text(encoding="utf-8"))
health = json.loads((directory / "health.json").read_text(encoding="utf-8"))
chat = json.loads((directory / "chat.json").read_text(encoding="utf-8"))
a2a = json.loads((directory / "a2a.json").read_text(encoding="utf-8"))
assert live["status"] == "ok"
assert health["status"] == "ok"
assert chat["status"] == "sucesso"
assert chat["fontes"], "a resposta RAG não indicou fontes"
assert "result" in a2a and "message" in a2a["result"]
PY

echo "Evidências salvas em $EVIDENCE_DIR."
