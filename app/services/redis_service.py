"""Redis remoto obrigatório para ranking de rotas."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class RedisUnavailable(RuntimeError):
    """Falha controlada ao acessar o Redis."""


class RedisSupport:
    def __init__(self, url: str, enabled: bool = True, timeout_seconds: float = 5) -> None:
        self.enabled = enabled
        self._client = None
        if enabled:
            try:
                import redis

                self._client = redis.Redis.from_url(
                    url,
                    socket_connect_timeout=timeout_seconds,
                    socket_timeout=timeout_seconds,
                    decode_responses=True,
                )
            except Exception as error:
                logger.warning("redis_configuracao_indisponivel", extra={"error_type": type(error).__name__})

    @classmethod
    def from_config(cls, config):
        return cls(config["REDIS_URL"], config["REDIS_ENABLED"], config["REDIS_TIMEOUT_SECONDS"])

    def health(self) -> str:
        if not self.enabled:
            return "desabilitado"
        try:
            return "disponivel" if self._client and self._client.ping() else "indisponivel"
        except Exception:
            return "indisponivel"

    def record_route(self, route: str) -> None:
        try:
            if not self._client:
                raise RedisUnavailable("Redis não configurado.")
            self._client.zincrby("apolloai:ranking:rotas", 1, route)
        except RedisUnavailable:
            raise
        except Exception as error:
            logger.warning("redis_indisponivel", extra={"error_type": type(error).__name__})
            raise RedisUnavailable("Não foi possível registrar a rota no Redis.") from error
