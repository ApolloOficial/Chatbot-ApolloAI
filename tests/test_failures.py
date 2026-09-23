from __future__ import annotations

import mongomock

from app import create_app
from app.llms import ProviderUnavailable
from app.memory import MongoMemoryRepository
from app.services.chat_service import ChatService
from app.services.mcp_client import MCPUnavailable
from app.services.redis_service import RedisUnavailable
from tests.conftest import FakeRedis, FakeRetriever, FakeRuntime, FakeSemanticStore


class UnhealthyMemory:
    def verify_ownership(self, *_): return True
    def health(self): return "indisponivel"


class ProviderFailure(FakeRuntime):
    def invoke(self, name, content):
        raise ProviderUnavailable("falha simulada")


class MCPFailure:
    def retrieve(self, query, route):
        raise MCPUnavailable("falha simulada")


class InvalidRouter(FakeRuntime):
    def invoke(self, name, content):
        if name == "roteador":
            return "{}"
        return super().invoke(name, content)


class RedisWriteFailure(FakeRedis):
    def record_route(self, route):
        raise RedisUnavailable("falha simulada")


def _client(memory, runtime, retriever):
    app = create_app({"TESTING": True, "AUTH_REQUIRED": False, "MONGODB_REQUIRED": True})
    service = ChatService(app.config, memory, FakeRedis(), app.extensions["metrics"], runtime, retriever)
    app.extensions["apollo_services"]["chat"] = service
    return app.test_client()


def _client_with_redis(memory, runtime, retriever, redis):
    app = create_app({"TESTING": True, "AUTH_REQUIRED": False, "MONGODB_REQUIRED": True})
    service = ChatService(app.config, memory, redis, app.extensions["metrics"], runtime, retriever)
    app.extensions["apollo_services"]["chat"] = service
    return app.test_client()


def test_mongodb_failure_is_controlled(payload):
    response = _client(UnhealthyMemory(), FakeRuntime(), FakeRetriever()).post("/chat", json=payload)
    assert response.status_code == 503
    assert response.json["status"] == "erro"
    assert "mongodb" not in response.json["resposta"].lower()


def test_ai_provider_failure_is_controlled(payload):
    memory = MongoMemoryRepository("mongodb://unused", "test", client=mongomock.MongoClient(),
                                   semantic_store=FakeSemanticStore())
    memory.health = lambda: "disponivel"
    response = _client(memory, ProviderFailure(), FakeRetriever()).post("/chat", json=payload)
    assert response.status_code == 503
    assert response.json["status"] == "erro"


def test_mcp_failure_is_controlled(payload):
    memory = MongoMemoryRepository("mongodb://unused", "test", client=mongomock.MongoClient(),
                                   semantic_store=FakeSemanticStore())
    memory.health = lambda: "disponivel"
    response = _client(memory, FakeRuntime(), MCPFailure()).post("/chat", json=payload)
    assert response.status_code == 503
    assert response.json["status"] == "erro"


def test_invalid_router_output_has_no_deterministic_fallback(payload):
    memory = MongoMemoryRepository("mongodb://unused", "test", client=mongomock.MongoClient(),
                                   semantic_store=FakeSemanticStore())
    memory.health = lambda: "disponivel"
    response = _client(memory, InvalidRouter(), FakeRetriever()).post("/chat", json=payload)
    assert response.status_code == 503
    assert response.json["status"] == "erro"


def test_redis_write_failure_has_no_silent_fallback(payload):
    memory = MongoMemoryRepository("mongodb://unused", "test", client=mongomock.MongoClient(),
                                   semantic_store=FakeSemanticStore())
    memory.health = lambda: "disponivel"
    response = _client_with_redis(
        memory, FakeRuntime(), FakeRetriever(), RedisWriteFailure(),
    ).post("/chat", json=payload)
    assert response.status_code == 503
    assert response.json["status"] == "erro"
