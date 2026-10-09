"""Embeddings locais e armazenamento vetorial remoto de documentos e resumos no Qdrant."""

from __future__ import annotations

import logging
import math
import threading
import uuid
from typing import Any
from urllib.parse import urlparse

from app.config import is_local_hostname

COLLECTION_MEMORY = "memoria_resumos_v2"
COLLECTION_DOCUMENTS = "rag_chunks_v2"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EMBEDDING_DIMENSIONS = 384
logger = logging.getLogger(__name__)
_EMBEDDING_MODELS: dict[tuple[str, str | None], Any] = {}
_EMBEDDING_MODELS_LOCK = threading.Lock()


class QdrantUnavailable(RuntimeError):
    """O índice vetorial não está configurado ou não respondeu."""


class QdrantSemanticStore:
    """Qdrant com embeddings multilíngues locais e sem chamadas de embedding pagas."""

    def __init__(self, url: str | None, api_key: str | None,
                 dimensions: int = EMBEDDING_DIMENSIONS, min_score: float = 0.35,
                 timeout_seconds: float = 10, cache_dir: str | None = None, embedding_model=None) -> None:
        if dimensions != EMBEDDING_DIMENSIONS:
            raise ValueError(
                f"{EMBEDDING_MODEL} gera vetores de {EMBEDDING_DIMENSIONS} dimensões; "
                f"QDRANT_VECTOR_SIZE={dimensions} é incompatível."
            )
        if not 0 <= min_score <= 1:
            raise ValueError("RAG_MIN_SCORE deve estar entre 0 e 1 para similaridade cosseno.")
        self.url, self.api_key = url, api_key
        self.dimensions = dimensions
        self.min_score = min_score
        self.timeout_seconds = timeout_seconds
        self.cache_dir = cache_dir
        self._embedding_model = embedding_model
        self.collection_memory = COLLECTION_MEMORY
        self.collection_documents = COLLECTION_DOCUMENTS
        self._client = None
        self._ready = False

    @classmethod
    def from_config(cls, config: dict[str, Any]):
        return cls(config.get("QDRANT_URL"), config.get("QDRANT_API_KEY"),
                   int(config.get("QDRANT_VECTOR_SIZE", EMBEDDING_DIMENSIONS)),
                   float(config.get("RAG_MIN_SCORE", 0.35)),
                   float(config.get("QDRANT_TIMEOUT_SECONDS", 10)),
                   config.get("FASTEMBED_CACHE_DIR"))

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
            collections = (self.collection_documents, self.collection_memory)
            return all(client.collection_exists(name) and self._collection_dimensions_match(client, name)
                       for name in collections) and client.count(self.collection_documents, exact=True).count > 0
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
        for name in (self.collection_memory, self.collection_documents):
            if client.collection_exists(name):
                if not self._collection_dimensions_match(client, name):
                    raise QdrantUnavailable(
                        f"A coleção {name} não usa embeddings de {self.dimensions} dimensões. "
                        "Exclua e recrie as coleções antes de reindexar."
                    )
            else:
                client.create_collection(name, vectors_config=vectors)
        try:
            client.create_payload_index(collection_name=self.collection_memory, field_name="user_id",
                                        field_schema=models.PayloadSchemaType.KEYWORD)
        except Exception as error:
            if "already exists" not in str(error).lower():
                raise
        self._ready = True

    def _collection_dimensions_match(self, client, collection_name: str) -> bool:
        info = client.get_collection(collection_name)
        vector_config = info.config.params.vectors
        if isinstance(vector_config, dict):
            vector_config = vector_config.get("")
        return getattr(vector_config, "size", None) == self.dimensions

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
        return self._embed([text])[0]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._embed(texts)

    def _embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        try:
            model = self._get_embedding_model()
            vectors = [
                [float(value) for value in vector]
                for vector in model.embed(texts, batch_size=32)
            ]
        except Exception as error:
            logger.warning("embedding_local_indisponivel", extra={"error_type": type(error).__name__})
            raise QdrantUnavailable(
                "Não foi possível carregar o modelo local de embeddings multilíngues."
            ) from error
        if len(vectors) != len(texts) or any(
            len(vector) != self.dimensions or not all(math.isfinite(value) for value in vector)
            for vector in vectors
        ):
            raise QdrantUnavailable("O modelo de embeddings retornou vetores inválidos ou incompatíveis.")
        return vectors

    def _get_embedding_model(self):
        if self._embedding_model is not None:
            return self._embedding_model
        key = (EMBEDDING_MODEL, self.cache_dir)
        with _EMBEDDING_MODELS_LOCK:
            if key not in _EMBEDDING_MODELS:
                from fastembed import TextEmbedding

                _EMBEDDING_MODELS[key] = TextEmbedding(
                    model_name=EMBEDDING_MODEL,
                    cache_dir=self.cache_dir,
                )
            self._embedding_model = _EMBEDDING_MODELS[key]
        return self._embedding_model

    @staticmethod
    def point_id(namespace: str, value: str) -> str:
        return str(uuid.uuid5(uuid.UUID("92c85a74-8769-4c83-b5c6-925088162db4"), f"{namespace}:{value}"))

    def upsert_summary(self, user_id: str, session_id: str, summary: str, created_at: str) -> None:
        self.upsert_summaries([{
            "user_id": user_id, "session_id": session_id, "summary": summary, "created_at": created_at,
        }])

    def upsert_summaries(self, summaries: list[dict[str, Any]]) -> None:
        if not summaries:
            return
        client, models = self._dependencies()
        vectors = self.embed_documents([item["summary"] for item in summaries])
        points = [models.PointStruct(
            id=self.point_id("summary", f"{item['user_id']}:{item['session_id']}"),
            vector=vector,
            payload={
                "user_id": item["user_id"], "session_id": item["session_id"],
                "resumo": item["summary"], "created_at": item.get("created_at"),
            },
        ) for item, vector in zip(summaries, vectors)]
        client.upsert(collection_name=self.collection_memory, points=points, wait=True)

    def search_summaries(self, user_id: str, query: str, limit: int) -> list[dict[str, Any]]:
        client, models = self._dependencies()
        result = client.query_points(collection_name=self.collection_memory, query=self.embed_query(query), limit=limit,
            query_filter=models.Filter(must=[models.FieldCondition(key="user_id", match=models.MatchValue(value=user_id))]),
            with_payload=True)
        return [
            dict(point.payload or {}, score=round(float(point.score), 4))
            for point in result.points if float(point.score) >= self.min_score
        ]

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

    def search_document_chunks(
        self, query: str, limit: int, query_vector: list[float] | None = None,
    ) -> list[dict[str, Any]]:
        client, _ = self._dependencies()
        vector = query_vector if query_vector is not None else self.embed_query(query)
        if len(vector) != self.dimensions or not all(math.isfinite(value) for value in vector):
            raise QdrantUnavailable("O vetor de consulta é inválido ou incompatível com a coleção.")
        result = client.query_points(collection_name=self.collection_documents, query=vector,
                                     limit=limit * 4, with_payload=True)
        matches = [dict(point.payload or {}, score=round(float(point.score), 4)) for point in result.points]
        matches = [item for item in matches if item["score"] >= self.min_score]
        return matches[:limit]
