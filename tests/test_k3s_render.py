from argparse import ArgumentTypeError, Namespace
from types import SimpleNamespace

import pytest

from deploy.k3s import render as renderer


BASE_MANIFEST = """apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
        - name: apolloai
          image: ghcr.io/apollooficial/chatbot-apolloai:sha-old
"""


def _arguments(host: str) -> Namespace:
    return Namespace(
        host=host,
        cors_origin=f"https://{host}",
        qdrant_url="https://qdrant.example.com",
        image_tag="sha-" + "0" * 40,
        acme_email="equipe@example.com",
        kubectl="kubectl",
    )


def test_public_host_accepts_public_ipv4_and_rejects_private_ipv4():
    assert renderer._public_host("8.8.8.8") == "8.8.8.8"
    with pytest.raises(ArgumentTypeError, match="IPv4 deve ser público"):
        renderer._public_host("10.0.0.1")


def test_ip_render_uses_short_lived_certificate_and_default_tls_store(monkeypatch):
    monkeypatch.setattr(
        renderer.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(stdout=BASE_MANIFEST),
    )

    manifest = renderer.render(_arguments("8.8.8.8"))

    assert 'PUBLIC_BASE_URL: "https://8.8.8.8"' in manifest
    assert "profile: shortlived" in manifest
    assert "kind: Certificate" in manifest
    assert "ipAddresses:\n    - 8.8.8.8" in manifest
    assert "kind: TLSStore" in manifest
    assert "host: 8.8.8.8" not in manifest


def test_domain_render_keeps_standard_acme_ingress(monkeypatch):
    monkeypatch.setattr(
        renderer.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(stdout=BASE_MANIFEST),
    )

    manifest = renderer.render(_arguments("api.example.com"))

    assert "name: letsencrypt-production" in manifest
    assert "profile: shortlived" not in manifest
    assert "kind: TLSStore" not in manifest
    assert "host: api.example.com" in manifest
