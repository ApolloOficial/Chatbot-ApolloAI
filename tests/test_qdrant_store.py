from types import SimpleNamespace

import pytest
from qdrant_client import models

from app.qdrant_store import COLLECTION_DOCUMENTS, COLLECTION_MEMORY, QdrantSemanticStore, QdrantUnavailable


def test_local_embeddings_use_original_collection_names_without_gemini():
    store = QdrantSemanticStore("https://qdrant.example.com", "test-key")

    assert store.configured
    assert store.collection_documents == COLLECTION_DOCUMENTS == "rag_chunks"
    assert store.collection_memory == COLLECTION_MEMORY == "memoria_resumos"
    document = store.embed_documents(["Photovoltaic module maintenance"])[0]
    query = store.embed_query("module maintenance")

    assert len(document) == len(query) == 768
    assert sum(a * b for a, b in zip(document, query)) > 0


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
    store._ready = True
    monkeypatch.setattr(store, "_dependencies", lambda: (FakeClient(), models))

    assert store.search_document_chunks("module maintenance", 1)
    assert store.search_summaries("user-1", "module maintenance", 1)
    assert [call["collection_name"] for call in calls] == [COLLECTION_DOCUMENTS, COLLECTION_MEMORY]


def test_fresh_index_refuses_existing_points(monkeypatch):
    class FakeClient:
        def count(self, collection_name, exact):
            assert exact
            return SimpleNamespace(count=1 if collection_name == COLLECTION_DOCUMENTS else 0)

    store = QdrantSemanticStore("https://qdrant.example.com", "test-key")
    monkeypatch.setattr(store, "_dependencies", lambda: (FakeClient(), models))

    with pytest.raises(QdrantUnavailable, match="rag_chunks"):
        store.require_empty_collections()
