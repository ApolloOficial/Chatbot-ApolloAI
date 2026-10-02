from types import SimpleNamespace

import pytest
from qdrant_client import models

from app.qdrant_store import (
    COLLECTION_DOCUMENTS, COLLECTION_MEMORY, EMBEDDING_DIMENSIONS,
    EMBEDDING_MODEL, QdrantSemanticStore, QdrantUnavailable,
)
from app.services.mcp_client import MCPRetriever


def test_local_embeddings_use_multilingual_model_and_original_collection_names():
    class FakeEmbeddingModel:
        def __init__(self):
            self.calls = []

        def embed(self, texts, batch_size):
            self.calls.append((texts, batch_size))
            return [[1.0] + [0.0] * (EMBEDDING_DIMENSIONS - 1) for _ in texts]

    model = FakeEmbeddingModel()
    store = QdrantSemanticStore("https://qdrant.example.com", "test-key", embedding_model=model)

    assert store.configured
    assert store.collection_documents == COLLECTION_DOCUMENTS == "rag_chunks_v2"
    assert store.collection_memory == COLLECTION_MEMORY == "memoria_resumos_v2"
    document = store.embed_documents(["Photovoltaic module maintenance"])[0]
    query = store.embed_query("module maintenance")

    assert EMBEDDING_MODEL == "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    assert len(document) == len(query) == EMBEDDING_DIMENSIONS == 384
    assert sum(a * b for a, b in zip(document, query)) > 0
    assert len(model.calls) == 2


def test_document_and_memory_queries_use_original_collections(monkeypatch):
    calls = []

    class FakeClient:
        def query_points(self, **kwargs):
            calls.append(kwargs)
            payload = ({"trecho": "Photovoltaic module maintenance"}
                       if kwargs["collection_name"] == COLLECTION_DOCUMENTS
                       else {"resumo": "Photovoltaic module maintenance"})
            return SimpleNamespace(points=[SimpleNamespace(payload=payload, score=0.9)])

    store = QdrantSemanticStore("https://qdrant.example.com", "test-key")
    store._embedding_model = SimpleNamespace(
        embed=lambda texts, batch_size: [[1.0] + [0.0] * (EMBEDDING_DIMENSIONS - 1) for _ in texts],
    )
    store._ready = True
    monkeypatch.setattr(store, "_dependencies", lambda: (FakeClient(), models))

    # A recuperação vetorial não deve ser descartada por falta de palavras idênticas.
    assert store.search_document_chunks(
        "What could explain lower energy output?", 1, query_vector=[0.0] * EMBEDDING_DIMENSIONS,
    )
    assert store.search_summaries("user-1", "module maintenance", 1)
    assert [call["collection_name"] for call in calls] == [COLLECTION_DOCUMENTS, COLLECTION_MEMORY]


def test_document_search_rejects_scores_below_relevance_threshold(monkeypatch):
    class FakeClient:
        def query_points(self, **kwargs):
            return SimpleNamespace(points=[SimpleNamespace(payload={"trecho": "Unrelated text"}, score=0.2)])

    store = QdrantSemanticStore("https://qdrant.example.com", "test-key", min_score=0.35)
    monkeypatch.setattr(store, "_dependencies", lambda: (FakeClient(), models))

    assert store.search_document_chunks("solar modules", 5, query_vector=[0.0] * EMBEDDING_DIMENSIONS) == []


def test_mcp_retriever_sends_query_embedding_to_server():
    calls = []

    class FakeClient:
        def search(self, tool, query, query_vector):
            calls.append((tool, query, query_vector))
            return []

    class FakeEmbeddingStore:
        def embed_query(self, query):
            return [0.5] * EMBEDDING_DIMENSIONS

    retriever = MCPRetriever(FakeClient(), FakeEmbeddingStore())
    retriever.retrieve("perda de geração", "ativos_solares")

    assert calls == [
        ("buscar_conhecimento_solar", "perda de geração", [0.5] * EMBEDDING_DIMENSIONS),
    ]


def test_fresh_index_refuses_existing_points(monkeypatch):
    class FakeClient:
        def count(self, collection_name, exact):
            assert exact
            return SimpleNamespace(count=1 if collection_name == COLLECTION_DOCUMENTS else 0)

    store = QdrantSemanticStore("https://qdrant.example.com", "test-key")
    monkeypatch.setattr(store, "_dependencies", lambda: (FakeClient(), models))

    with pytest.raises(QdrantUnavailable, match="rag_chunks"):
        store.require_empty_collections()


def test_existing_collection_with_old_dimension_is_rejected(monkeypatch):
    class FakeClient:
        def collection_exists(self, collection_name):
            return True

        def get_collection(self, collection_name):
            return SimpleNamespace(config=SimpleNamespace(
                params=SimpleNamespace(vectors=SimpleNamespace(size=768)),
            ))

    store = QdrantSemanticStore("https://qdrant.example.com", "test-key")
    monkeypatch.setattr(store, "_dependencies", lambda: (FakeClient(), models))

    with pytest.raises(QdrantUnavailable, match="384 dimensões"):
        store.ensure_collections()
