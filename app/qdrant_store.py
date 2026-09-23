"""Vetores locais no Qdrant para documentos e resumos de sessões.

O MongoDB continua sendo a fonte de verdade da memória. Este módulo guarda
somente vetores e payloads suficientes para recuperar os dados semanticamente.
"""

from __future__ import annotations

import uuid
from typing import Any
from urllib.parse import urlparse

from app.config import is_local_hostname

COLLECTION_MEMORY = "memoria_resumos"
COLLECTION_DOCUMENTS = "rag_chunks"


class QdrantUnavailable(RuntimeError):
    """O índice vetorial não está configurado ou não respondeu."""


class QdrantSemanticStore:
    """Cliente sob demanda com hashing local, sem API de embeddings."""

    def __init__(self, url: str | None, api_key: str | None,
                 dimensions: int = 768, min_score: float = 0.08, timeout_seconds: float = 10) -> None:
        self.url, self.api_key = url, api_key
        self.dimensions = dimensions
        self.min_score = min_score
        self.timeout_seconds = timeout_seconds
        self.collection_memory = COLLECTION_MEMORY
        self.collection_documents = COLLECTION_DOCUMENTS
        self._client = None
        self._ready = False

    @classmethod
    def from_config(cls, config: dict[str, Any]):
        return cls(config.get("QDRANT_URL"), config.get("QDRANT_API_KEY"),
                   int(config.get("QDRANT_VECTOR_SIZE", 768)), float(config.get("RAG_MIN_SCORE", 0.08)),
                   float(config.get("QDRANT_TIMEOUT_SECONDS", 10)))

    @property
    def configured(self) -> bool:
        parsed = urlparse(self.url or "")
        return bool(
            parsed.scheme == "https"
            and not is_local_hostname(parsed.hostname)
            and self.api_key
        )

    def is_ready(self) -> bool:
        try:
            client, _ = self._dependencies()
            return (
                client.collection_exists(self.collection_documents)
                and client.collection_exists(self.collection_memory)
                and client.count(self.collection_documents, exact=True).count > 0
            )
        except Exception:
            return False

    def _dependencies(self):
        if not self.configured:
            raise QdrantUnavailable("Configure QDRANT_URL HTTPS remota e QDRANT_API_KEY.")
        try:
            from qdrant_client import QdrantClient, models
        except ImportError as error:
            raise QdrantUnavailable("Instale qdrant-client para habilitar o índice vetorial.") from error
        if self._client is None:
            self._client = QdrantClient(
                url=self.url, api_key=self.api_key, timeout=self.timeout_seconds, check_compatibility=False,
            )
        return self._client, models

    def ensure_collections(self) -> None:
        if self._ready:
            return
        client, models = self._dependencies()
        vectors = models.VectorParams(size=self.dimensions, distance=models.Distance.COSINE)
        if not client.collection_exists(self.collection_memory):
            client.create_collection(self.collection_memory, vectors_config=vectors)
        if not client.collection_exists(self.collection_documents):
            client.create_collection(self.collection_documents, vectors_config=vectors)
        try:
            client.create_payload_index(collection_name=self.collection_memory, field_name="user_id",
                                        field_schema=models.PayloadSchemaType.KEYWORD)
        except Exception as error:
            if "already exists" not in str(error).lower():
                raise
        self._ready = True

    def require_empty_collections(self) -> None:
        """Impede misturar vetores antigos com uma indexação remota nova."""
        client, _ = self._dependencies()
        occupied = [name for name in (self.collection_documents, self.collection_memory)
                    if client.count(name, exact=True).count]
        if occupied:
            raise QdrantUnavailable(
                f"Exclua as coleções antes da indexação do zero: {', '.join(occupied)}"
            )

    def embed_query(self, text: str) -> list[float]:
        from app.services.rag import _embed_tokens, _query_tokens

        return self._dense_local_vector(_embed_tokens(_query_tokens(text), self.dimensions))

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        from app.services.rag import _embed

        return [self._dense_local_vector(_embed(text, self.dimensions)) for text in texts]

    def _dense_local_vector(self, sparse: list[list[int | float]]) -> list[float]:
        vector = [0.0] * self.dimensions
        for index, value in sparse:
            vector[int(index)] = float(value)
        return vector

    @staticmethod
    def point_id(namespace: str, value: str) -> str:
        return str(uuid.uuid5(uuid.UUID("92c85a74-8769-4c83-b5c6-925088162db4"), f"{namespace}:{value}"))

    def upsert_summary(self, user_id: str, session_id: str, summary: str, created_at: str) -> None:
        client, models = self._dependencies()
        client.upsert(collection_name=self.collection_memory, points=[models.PointStruct(
            id=self.point_id("summary", f"{user_id}:{session_id}"), vector=self.embed_query(summary),
            payload={"user_id": user_id, "session_id": session_id, "resumo": summary, "created_at": created_at},
        )], wait=True)

    def search_summaries(self, user_id: str, query: str, limit: int) -> list[dict[str, Any]]:
        client, models = self._dependencies()
        result = client.query_points(collection_name=self.collection_memory, query=self.embed_query(query), limit=limit,
            query_filter=models.Filter(must=[models.FieldCondition(key="user_id", match=models.MatchValue(value=user_id))]),
            with_payload=True)
        return [dict(point.payload or {}, score=round(float(point.score), 4)) for point in result.points]

    def upsert_document_chunks(self, chunks: list[dict[str, Any]]) -> None:
        """Indexa todos os chunks; IDs estáveis tornam a reindexação idempotente."""
        self.ensure_collections()
        client, models = self._dependencies()
        vectors = self.embed_documents([chunk["trecho"] for chunk in chunks])
        points = []
        for chunk, vector in zip(chunks, vectors):
            payload = {key: chunk.get(key) for key in ("documento", "pagina", "secao", "url", "trecho")}
            points.append(models.PointStruct(
                id=self.point_id("document", chunk["id"]), vector=vector, payload=payload,
            ))
        client.upsert(collection_name=self.collection_documents, points=points, wait=True)

    def search_document_chunks(self, query: str, limit: int) -> list[dict[str, Any]]:
        client, _ = self._dependencies()
        result = client.query_points(collection_name=self.collection_documents, query=self.embed_query(query),
                                     limit=limit * 4, with_payload=True)
        matches = [dict(point.payload or {}, score=round(float(point.score), 4)) for point in result.points]
        from app.services.rag import _query_tokens, _tokens

        query_terms = set(_query_tokens(query))
        matches = [item for item in matches if item["score"] >= self.min_score
                   and query_terms.intersection(_tokens(item.get("trecho", "")))]
        return matches[:limit]
