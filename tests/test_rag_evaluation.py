from pathlib import Path
import os

import pytest

from app.config import BASE_DIR, Config
from app.services.rag import SolarKnowledgeBase
from app.services.rag_evaluation import evaluate, load_cases


@pytest.mark.integration
@pytest.mark.skipif(os.getenv("RUN_RAG_EVALUATION") != "1", reason="requer Qdrant remoto indexado")
def test_versioned_rag_evaluation_meets_quality_floor():
    cases = load_cases(Path(BASE_DIR) / "data" / "solar" / "rag_eval.json")
    report = evaluate(SolarKnowledgeBase.from_config(Config.__dict__), cases)
    assert report["passed"], report["details"]
    assert report["hit_rate_at_k"] == 1.0
    assert report["irrelevant_rejection_rate"] == 1.0
