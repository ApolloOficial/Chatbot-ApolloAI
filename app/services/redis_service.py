"""Redis opcional para cache, fila e ranking; nunca persiste o histórico."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class RedisSupport:
    def __init__(self, url: str, enabled: bool = True) -> None:
        self.enabled = enabled
        self._client = None
        if enabled:
            try:
                import redis

                self._client = redis.Redis.from_url(url, socket_connect_timeout=0.5, socket_timeout=0.5, decode_responses=True)
            except Exception as error:
                logger.warning("redis_configuracao_indisponivel", extra={"error_type": type(error).__name__})

    @classmethod
    def from_config(cls, config):
        return cls(config["REDIS_URL"], config["REDIS_ENABLED"])

    def health(self) -> str:
        if not self.enabled:
            return "desabilitado"
        try:
            return "disponivel" if self._client and self._client.ping() else "indisponivel"
        except Exception:
            return "indisponivel"

    def record_route(self, route: str) -> None:
        try:
            if self._client:
                self._client.zincrby("apolloai:ranking:rotas", 1, route)
        except Exception as error:
            logger.warning("redis_degradado", extra={"error_type": type(error).__name__})

    def enqueue_indexing(self, document: str) -> bool:
        try:
            return bool(self._client and self._client.rpush("apolloai:fila:indexacao", document))
        except Exception as error:
            logger.warning("redis_fila_indisponivel", extra={"error_type": type(error).__name__})
            return False
