"""Autentica o cliente Apollo e fornece uma identidade de usuário confiável."""

from __future__ import annotations

import hmac
import re

from flask import Request


class AuthenticationRequired(RuntimeError):
    """Credenciais ausentes ou inválidas."""


class TrustedIdentityRequired(RuntimeError):
    """Identidade do usuário final ausente ou inválida."""


_USER_ID = re.compile(r"^[A-Za-z0-9_.:@-]{3,128}$")


def trusted_user_id(request: Request, config, body_user_id: str | None = None) -> str | None:
    """Valida Bearer e usa a identidade propagada pelo backend Apollo quando exigido."""
    if not config.get("AUTH_REQUIRED", False):
        return body_user_id

    authorization = request.headers.get("Authorization", "")
    scheme, _, credential = authorization.partition(" ")
    expected = str(config.get("APOLLOAI_API_TOKEN") or "")
    if scheme.lower() != "bearer" or not credential or not expected or not hmac.compare_digest(credential, expected):
        raise AuthenticationRequired

    identity = request.headers.get("X-User-ID", "").strip()
    if not _USER_ID.fullmatch(identity) or ("@" in identity and "." in identity.split("@")[-1]):
        raise TrustedIdentityRequired
    return identity
