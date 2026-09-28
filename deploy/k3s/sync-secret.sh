#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="${APOLLOAI_NAMESPACE:-apolloai-hml}"
: "${AWS_SECRET_ID:?Configure AWS_SECRET_ID}"
: "${AWS_REGION:?Configure AWS_REGION}"

SECRET_JSON="$(mktemp)"
SECRET_ENV="$(mktemp)"
trap 'rm -f -- "$SECRET_JSON" "$SECRET_ENV"' EXIT
chmod 600 "$SECRET_JSON" "$SECRET_ENV"

aws sts get-caller-identity >/dev/null
aws secretsmanager get-secret-value \
  --region "$AWS_REGION" \
  --secret-id "$AWS_SECRET_ID" \
  --query SecretString \
  --output text >"$SECRET_JSON"

python3 - "$SECRET_JSON" "$SECRET_ENV" <<'PY'
import json
import sys

required = ("APOLLOAI_API_TOKEN", "GROQ_API_KEY", "QDRANT_API_KEY", "MONGODB_URI", "REDIS_URL")
with open(sys.argv[1], encoding="utf-8") as source:
    values = json.load(source)
missing = [name for name in required if not isinstance(values.get(name), str) or not values[name]]
if missing:
    raise SystemExit("Chaves ausentes no Secrets Manager: " + ", ".join(missing))
with open(sys.argv[2], "w", encoding="utf-8", newline="\n") as destination:
    for name in required:
        value = values[name]
        if "\n" in value or "\r" in value:
            raise SystemExit(f"O valor de {name} não pode conter quebra de linha")
        destination.write(f"{name}={value}\n")
PY

kubectl -n "$NAMESPACE" create secret generic apolloai-secrets \
  --from-env-file="$SECRET_ENV" \
  --dry-run=client \
  --output=yaml | kubectl apply -f - >/dev/null

echo "Secret apolloai-secrets sincronizado no namespace ${NAMESPACE}."
