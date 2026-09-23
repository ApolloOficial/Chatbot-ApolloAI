from types import ModuleType, SimpleNamespace
import sys

import pytest

from app import create_app
from app.llms import LangChainAgentRuntime, ProviderUnavailable
from app.qdrant_store import QdrantSemanticStore


REMOTE_CONFIG = {
    "PUBLIC_BASE_URL": "https://apolloai.example.com",
    "CORS_ORIGINS": ["https://apollo.example.com"],
    "QDRANT_URL": "https://qdrant.example.com",
    "QDRANT_API_KEY": "test-key",
    "MONGODB_URI": "mongodb+srv://user:password@mongo.example.com/apollo",
    "REDIS_URL": "rediss://redis.example.com:6380/0",
    "APOLLOAI_API_TOKEN": "test-token",
    "AUTH_REQUIRED": True,
    "MONGODB_REQUIRED": True,
    "REDIS_ENABLED": True,
    "REDIS_REQUIRED": True,
    "MCP_REQUIRED": True,
    "AI_PROVIDER": "bedrock",
    "AI_MODEL": "us.anthropic.claude-sonnet-4-6",
    "AWS_REGION": "us-east-1",
}


def test_app_accepts_remote_services_without_connecting_to_them():
    app = create_app(REMOTE_CONFIG)
    assert app.config["QDRANT_API_KEY"] == "test-key"


@pytest.mark.parametrize("field,value", [
    ("QDRANT_URL", "http://localhost:6333"),
    ("QDRANT_URL", "https://host.docker.internal:6333"),
    ("QDRANT_API_KEY", ""),
    ("MONGODB_URI", "mongodb://mongo:27017"),
    ("REDIS_URL", "redis://redis:6379/0"),
    ("CORS_ORIGINS", ["http://localhost:5000"]),
    ("AWS_REGION", None),
])
def test_app_rejects_local_or_incomplete_configuration(field, value):
    with pytest.raises(ValueError, match=field):
        create_app(REMOTE_CONFIG | {field: value})


def test_bedrock_uses_selected_model_and_aws_region(monkeypatch):
    received = {}
    module = ModuleType("langchain_aws")

    def fake_model(**kwargs):
        received.update(kwargs)
        return object()

    module.ChatBedrockConverse = fake_model
    monkeypatch.setitem(sys.modules, "langchain_aws", module)
    runtime = LangChainAgentRuntime({
        "AI_PROVIDER": "bedrock", "AI_MODEL": "us.anthropic.claude-sonnet-4-6",
        "AWS_REGION": "us-east-1", "AI_TIMEOUT_SECONDS": 30, "AI_MAX_RETRIES": 1,
    })
    runtime.model
    assert received["model"] == "us.anthropic.claude-sonnet-4-6"
    assert received["region_name"] == "us-east-1"


def test_classifier_failure_does_not_approve_input():
    runtime = LangChainAgentRuntime({})
    runtime._model = SimpleNamespace(invoke=lambda _: (_ for _ in ()).throw(RuntimeError("offline")))
    with pytest.raises(ProviderUnavailable):
        runtime.classify_input("Como operar um inversor?")


def test_qdrant_readiness_requires_indexed_remote_collections(monkeypatch):
    store = QdrantSemanticStore("https://qdrant.example.com", "test-key")

    class Client:
        def collection_exists(self, name):
            return True

        def count(self, name, exact):
            return SimpleNamespace(count=0)

    monkeypatch.setattr(store, "_dependencies", lambda: (Client(), None))
    assert not store.is_ready()
