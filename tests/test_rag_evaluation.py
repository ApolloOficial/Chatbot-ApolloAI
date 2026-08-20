from pathlib import Path

from app.config import BASE_DIR, Config
from app.services.rag import SolarKnowledgeBase
from app.services.rag_evaluation import evaluate, load_cases


def test_versioned_rag_evaluation_meets_quality_floor():
    cases = load_cases(Path(BASE_DIR) / "data" / "solar" / "rag_eval.json")
    report = evaluate(SolarKnowledgeBase.from_config(Config.__dict__), cases)
    assert report["passed"], report["details"]
    assert report["hit_rate_at_k"] >= 0.8
    assert report["irrelevant_rejection_rate"] == 1.0
