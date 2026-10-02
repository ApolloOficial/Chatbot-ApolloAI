"""Cria as collections no Qdrant e indexa os chunks dos documentos solares.

Uso: python -m scripts.index_qdrant
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import Config
from app.qdrant_store import QdrantSemanticStore, QdrantUnavailable
from app.services.rag import SolarKnowledgeBase


def load_summaries(config: dict) -> list[dict]:
    """Lê resumos do Mongo para reconstruir a coleção semântica versionada."""
    from pymongo import MongoClient

    client = MongoClient(
        config["MONGODB_URI"], serverSelectionTimeoutMS=config["MONGODB_TIMEOUT_MS"],
        connectTimeoutMS=config["MONGODB_TIMEOUT_MS"], appname="ApolloAI-RAG-Reindex",
        tz_aware=True,
    )
    try:
        client.admin.command("ping")
        return list(client[config["MONGODB_DATABASE"]]["summaries"].find(
            {"summary": {"$type": "string", "$ne": ""}},
            {"_id": 0, "user_id": 1, "session_id": 1, "summary": 1,
             "updated_at": 1, "created_at": 1},
        ))
    finally:
        client.close()


def main() -> int:
    config = Config.__dict__
    store = QdrantSemanticStore.from_config(config)
    if not store.configured:
        raise SystemExit("Configure QDRANT_URL e, no Qdrant Cloud, QDRANT_API_KEY no .env.")
    try:
        summaries = load_summaries(config)
        print("[index] Lendo Markdown e preparando chunks...", flush=True)
        total = SolarKnowledgeBase.from_config(config).index_qdrant(
            store, int(config["QDRANT_INDEX_BATCH_SIZE"]),
            on_progress=lambda current, maximum: print(f"[index] {current}/{maximum} chunks indexados", flush=True),
        )
        for start in range(0, len(summaries), int(config["QDRANT_INDEX_BATCH_SIZE"])):
            batch = summaries[start:start + int(config["QDRANT_INDEX_BATCH_SIZE"])]
            store.upsert_summaries([{
                "user_id": item["user_id"], "session_id": item["session_id"],
                "summary": item["summary"],
                "created_at": (item.get("updated_at") or item.get("created_at")).isoformat(),
            } for item in batch])
            print(f"[index] {min(start + len(batch), len(summaries))}/{len(summaries)} resumos indexados", flush=True)
    except (QdrantUnavailable, ValueError) as error:
        raise SystemExit(str(error)) from error
    print(
        f"Qdrant pronto: collections {store.collection_memory} e {store.collection_documents}; "
        f"{total} chunks e {len(summaries)} resumos indexados."
    )
    return total


if __name__ == "__main__":
    main()
