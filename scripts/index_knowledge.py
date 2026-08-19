"""Indexa os documentos técnicos locais com metadados de página."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import Config
from app.services.rag import SolarKnowledgeBase


if __name__ == "__main__":
    knowledge = SolarKnowledgeBase.from_config(Config.__dict__)
    print(f"Chunks indexados: {knowledge.index_all()}")
