"""Dependências compartilhadas inicializadas pela application factory."""

from __future__ import annotations

from flask import Flask


def init_extensions(app: Flask) -> None:
    """Registra serviços com construção preguiçosa para não bloquear o startup."""
    from app.services.metrics import MetricsRegistry

    app.extensions["metrics"] = MetricsRegistry()
    app.extensions["apollo_services"] = {}


def get_service(app: Flask, name: str):
    """Retorna um serviço por aplicação, criando-o somente no primeiro uso."""
    services = app.extensions["apollo_services"]
    if name in services:
        return services[name]
    if name == "memory":
        from app.memory import MongoMemoryRepository

        service = MongoMemoryRepository.from_config(app.config)
    elif name == "chat":
        from app.services.chat_service import ChatService

        service = ChatService.from_app(app)
    elif name == "rag":
        from app.services.rag import SolarKnowledgeBase

        service = SolarKnowledgeBase.from_config(app.config)
    elif name == "redis":
        from app.services.redis_service import RedisSupport

        service = RedisSupport.from_config(app.config)
    else:
        raise KeyError(f"Serviço desconhecido: {name}")
    services[name] = service
    return service
