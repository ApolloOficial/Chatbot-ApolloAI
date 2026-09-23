"""Cria as collections no Qdrant e indexa os chunks dos documentos solares.

Uso: python -m scripts.index_qdrant
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import Config
from app.qdrant_store import QdrantSemanticStore, QdrantUnavailable
from app.services.rag import SolarKnowledgeBase


def main() -> int:
    config = Config.__dict__
    store = QdrantSemanticStore.from_config(config)
    if not store.configured:
        raise SystemExit("Configure QDRANT_URL e, no Qdrant Cloud, QDRANT_API_KEY no .env.")
    try:
        print("[index] Lendo Markdown e preparando chunks...", flush=True)
        total = SolarKnowledgeBase.from_config(config).index_qdrant(
            store, int(config["QDRANT_INDEX_BATCH_SIZE"]),
            on_progress=lambda current, maximum: print(f"[index] {current}/{maximum} chunks indexados", flush=True),
        )
    except (QdrantUnavailable, ValueError) as error:
        raise SystemExit(str(error)) from error
    print(f"Qdrant pronto: collections {store.collection_memory} e {store.collection_documents}; {total} chunks indexados.")
    return total


if __name__ == "__main__":
    main()
