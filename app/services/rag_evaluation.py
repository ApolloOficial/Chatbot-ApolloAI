"""Avaliação determinística da recuperação antes de mudanças no RAG."""

from __future__ import annotations

import json
import unicodedata
from pathlib import Path


def _normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def load_cases(path: Path) -> list[dict]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("version") != 1 or not isinstance(payload.get("cases"), list):
        raise ValueError("Dataset de avaliação RAG inválido.")
    return payload["cases"]


def evaluate(retriever, cases: list[dict]) -> dict:
    details = []
    relevant_total = relevant_hits = irrelevant_total = irrelevant_empty = 0
    reciprocal_rank_sum = 0.0
    for case in cases:
        results = retriever.retrieve(case["query"], "ativos_solares")
        if case["relevant"]:
            relevant_total += 1
            rank = _first_matching_rank(results, case["expected_terms"])
            hit = rank is not None
            relevant_hits += int(hit)
            reciprocal_rank_sum += 1 / rank if rank else 0
        else:
            irrelevant_total += 1
            hit = not results
            irrelevant_empty += int(hit)
            rank = None
        details.append({
            "id": case["id"], "passed": hit, "result_count": len(results),
            "first_relevant_rank": rank,
        })
    hit_rate = relevant_hits / relevant_total if relevant_total else 1.0
    rejection_rate = irrelevant_empty / irrelevant_total if irrelevant_total else 1.0
    return {
        "hit_rate_at_k": round(hit_rate, 4),
        "mean_reciprocal_rank": round(reciprocal_rank_sum / relevant_total, 4) if relevant_total else 1.0,
        "irrelevant_rejection_rate": round(rejection_rate, 4),
        "passed": hit_rate == 1.0 and rejection_rate == 1.0,
        "details": details,
    }


def _first_matching_rank(results: list[dict], expected_terms: list[str]) -> int | None:
    normalized_terms = [_normalize(term) for term in expected_terms]
    for rank, result in enumerate(results, 1):
        text = _normalize(result.get("trecho", ""))
        if all(term in text for term in normalized_terms):
            return rank
    return None
