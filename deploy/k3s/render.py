"""Renderiza os recursos do K3s sem gravar credenciais no repositório."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


IMAGE = "ghcr.io/apollooficial/chatbot-apolloai"
NAMESPACE = "apolloai-hml"


def _hostname(value: str) -> str:
    value = value.strip().lower()
    if not re.fullmatch(r"(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}", value):
        raise argparse.ArgumentTypeError("domínio inválido")
    return value


def _https_url(value: str) -> str:
    parsed = urlparse(value.strip())
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise argparse.ArgumentTypeError("a URL deve usar HTTPS e não pode conter credenciais")
    return value.rstrip("/")


def _image_tag(value: str) -> str:
    if not re.fullmatch(r"sha-[0-9a-f]{40}", value):
        raise argparse.ArgumentTypeError("a imagem deve usar uma tag sha-<commit completo>")
    return value


def _email(value: str) -> str:
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value):
        raise argparse.ArgumentTypeError("e-mail ACME inválido")
    return value


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _config_map(domain: str, cors_origin: str, qdrant_url: str) -> str:
    values = {
        "AUTH_REQUIRED": "true",
        "MONGODB_DATABASE": "apollo_ai_hml",
        "MONGODB_REQUIRED": "true",
        "REDIS_ENABLED": "true",
        "REDIS_REQUIRED": "true",
        "REDIS_TIMEOUT_SECONDS": "5",
        "MCP_REQUIRED": "true",
        "MCP_SERVER_COMMAND": "python -m app.mcp_server",
        "PUBLIC_BASE_URL": f"https://{domain}",
        "CORS_ORIGINS": cors_origin,
        "AI_PROVIDER": "groq",
        "AI_MODEL": "openai/gpt-oss-20b",
        "AI_TIMEOUT_SECONDS": "30",
        "AI_MAX_RETRIES": "1",
        "QDRANT_URL": qdrant_url,
        "QDRANT_VECTOR_SIZE": "768",
        "QDRANT_TIMEOUT_SECONDS": "10",
        "RAG_TOP_K": "5",
        "RAG_MIN_SCORE": "0.08",
        "AWS_LAB_BUDGET_USD": "50",
        "AWS_MONTHLY_COST_100_USERS": "12.80",
        "AWS_MONTHLY_COST_1000_USERS": "20.40",
        "AI_FREE_DAILY_REQUEST_LIMIT": "1000",
        "AI_FREE_DAILY_TOKEN_LIMIT": "200000",
    }
    data = "\n".join(f"  {key}: {_quoted(value)}" for key, value in values.items())
    return f"""apiVersion: v1
kind: ConfigMap
metadata:
  name: apolloai-config
  namespace: {NAMESPACE}
data:
{data}
"""


def _issuer(email: str) -> str:
    return f"""apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-production
spec:
  acme:
    email: {_quoted(email)}
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-production-account
    solvers:
      - http01:
          ingress:
            ingressClassName: traefik
"""


def _ingress(domain: str) -> str:
    return f"""apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: apolloai
  namespace: {NAMESPACE}
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-production
    traefik.ingress.kubernetes.io/router.entrypoints: web,websecure
    traefik.ingress.kubernetes.io/router.tls: "true"
spec:
  ingressClassName: traefik
  tls:
    - hosts:
        - {domain}
      secretName: apolloai-hml-tls
  rules:
    - host: {domain}
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: apolloai
                port:
                  name: http
"""


def render(args: argparse.Namespace) -> str:
    overlay = Path(__file__).resolve().parents[1] / "k8s" / "overlays" / "hml"
    base = subprocess.run(
        [args.kubectl, "kustomize", str(overlay)], check=True, capture_output=True, text=True,
    ).stdout
    image_pattern = rf"(?m)^(\s*image:\s*){re.escape(IMAGE)}:[^\s]+$"
    base, replacements = re.subn(image_pattern, rf"\g<1>{IMAGE}:{args.image_tag}", base)
    if replacements != 1:
        raise RuntimeError("não foi possível identificar uma única imagem ApolloAI no manifesto")
    documents = [base.rstrip(), _config_map(args.domain, args.cors_origin, args.qdrant_url).rstrip(),
                 _issuer(args.acme_email).rstrip(), _ingress(args.domain).rstrip()]
    rendered = "\n---\n".join(documents) + "\n"
    forbidden = (".invalid", "replace-with", "CHANGE_ME")
    if any(marker in rendered for marker in forbidden):
        raise RuntimeError("o manifesto renderizado ainda contém marcadores não substituídos")
    return rendered


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True, type=_hostname)
    parser.add_argument("--cors-origin", required=True, type=_https_url)
    parser.add_argument("--qdrant-url", required=True, type=_https_url)
    parser.add_argument("--image-tag", required=True, type=_image_tag)
    parser.add_argument("--acme-email", required=True, type=_email)
    parser.add_argument("--kubectl", default="kubectl")
    return parser.parse_args()


if __name__ == "__main__":
    try:
        sys.stdout.write(render(parse_args()))
    except (OSError, subprocess.CalledProcessError, RuntimeError) as error:
        print(f"erro: {error}", file=sys.stderr)
        raise SystemExit(1) from error
