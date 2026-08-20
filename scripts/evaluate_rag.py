"""Executa o conjunto versionado de avaliação do RAG local."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import BASE_DIR, Config
from app.services.rag import SolarKnowledgeBase
from app.services.rag_evaluation import evaluate, load_cases


def main() -> int:
    cases = load_cases(Path(BASE_DIR) / "data" / "solar" / "rag_eval.json")
    report = evaluate(SolarKnowledgeBase.from_config(Config.__dict__), cases)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
