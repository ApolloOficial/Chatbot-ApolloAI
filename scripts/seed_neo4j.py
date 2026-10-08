"""Carrega a pequena massa de dados do grafo Neo4j."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import Config
from app.services.neo4j_service import SolarGraph


if __name__ == "__main__":
    graph = SolarGraph.from_config(Config.__dict__)
    try:
        print(f"{graph.seed()} caminhos carregados no Neo4j.")
    finally:
        graph.close()
