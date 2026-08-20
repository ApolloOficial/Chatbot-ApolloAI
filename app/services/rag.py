"""Pipeline RAG local: PDF → chunks → embeddings → índice vetorial persistente."""

from __future__ import annotations

import hashlib
import json
import logging
import math
import re
from pathlib import Path
from typing import Any, Iterable

from pypdf import PdfReader

logger = logging.getLogger(__name__)

SOURCE_URLS = {
    "nrel_pv_om_best_practices_fact_sheet.pdf": "https://www.nrel.gov/docs/fy17osti/68281.pdf",
    "nrel_pv_om_best_practices_sintese.md": "https://www.nrel.gov/docs/fy17osti/68281.pdf",
}


class SolarKnowledgeBase:
    """Índice vetorial leve e reproduzível, sem API paga de embeddings."""

    dimensions = 4096

    def __init__(self, documents_dir: Path, index_path: Path, top_k: int = 5, min_score: float = 0.08):
        self.documents_dir = Path(documents_dir)
        self.index_path = Path(index_path)
        self.top_k = top_k
        self.min_score = min_score
        self._chunks: list[dict[str, Any]] | None = None

    @classmethod
    def from_config(cls, config):
        return cls(config["SOLAR_DOCUMENTS_DIR"], config["VECTOR_INDEX_PATH"], config["RAG_TOP_K"], config["RAG_MIN_SCORE"])

    @property
    def is_ready(self) -> bool:
        return self.index_path.is_file() or any(self._document_paths())

    def index_all(self) -> int:
        chunks: list[dict[str, Any]] = []
        for document_path in self._document_paths():
            if document_path.suffix.lower() == ".pdf":
                chunks.extend(self._extract_pdf(document_path))
            else:
                chunks.extend(self._extract_text(document_path))
        payload = {"version": 2, "embedding": "signed_feature_hashing_v1", "dimensions": self.dimensions, "chunks": chunks}
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.index_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        self._chunks = chunks
        logger.info("rag_indexado", extra={"documents": len(self._document_paths()), "chunks": len(chunks)})
        return len(chunks)

    def _document_paths(self) -> list[Path]:
        return sorted(path for path in self.documents_dir.iterdir() if path.suffix.lower() in {".pdf", ".md", ".txt"}) if self.documents_dir.is_dir() else []

    def _extract_pdf(self, path: Path) -> list[dict[str, Any]]:
        reader = PdfReader(str(path))
        result = []
        for page_number, page in enumerate(reader.pages, 1):
            text = _clean(page.extract_text() or "")
            for part_number, part in enumerate(_split(text), 1):
                result.append({
                    "id": f"{path.stem}-p{page_number}-c{part_number}",
                    "documento": path.name, "pagina": page_number,
                    "secao": _section(part), "url": SOURCE_URLS.get(path.name),
                    "trecho": part, "termos": sorted(set(_tokens(part))),
                    "embedding": _embed(part, self.dimensions),
                })
        return result

    def _extract_text(self, path: Path) -> list[dict[str, Any]]:
        text = path.read_text(encoding="utf-8")
        result = []
        for part_number, part in enumerate(_split(_clean(text)), 1):
            result.append({
                "id": f"{path.stem}-c{part_number}", "documento": path.name, "pagina": None,
                "secao": _section(part), "url": SOURCE_URLS.get(path.name), "trecho": part,
                "termos": sorted(set(_tokens(part))), "embedding": _embed(part, self.dimensions),
            })
        return result

    def _load(self) -> list[dict[str, Any]]:
        if self._chunks is not None:
            return self._chunks
        if not self.index_path.is_file():
            self.index_all()
        try:
            payload = json.loads(self.index_path.read_text(encoding="utf-8"))
            if payload.get("version") != 2 or payload.get("dimensions") != self.dimensions:
                return self._reindex()
            self._chunks = payload["chunks"]
        except (OSError, KeyError, json.JSONDecodeError) as error:
            logger.warning("rag_indice_invalido", extra={"error_type": type(error).__name__})
            self.index_all()
        return self._chunks or []

    def _reindex(self) -> list[dict[str, Any]]:
        self.index_all()
        return self._chunks or []

    def retrieve(self, query: str, route: str = "ativos_solares") -> list[dict[str, Any]]:
        del route
        query_vector = _embed(query, self.dimensions)
        query_terms = set(_tokens(query))
        scored = []
        for chunk in self._load():
            chunk_terms = set(chunk.get("termos", []))
            intersection = query_terms.intersection(chunk_terms)
            if not intersection:
                continue
            vector_score = max(0.0, _dot(query_vector, chunk["embedding"]))
            lexical_coverage = len(intersection) / max(len(query_terms), 1)
            score = 0.75 * vector_score + 0.25 * lexical_coverage
            if score >= self.min_score:
                public = {key: value for key, value in chunk.items() if key not in {"embedding", "id", "termos"}}
                public["score"] = round(score, 4)
                scored.append(public)
        scored.sort(key=lambda item: item["score"], reverse=True)
        return scored[: self.top_k]


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _split(text: str, size: int = 1200, overlap: int = 200) -> Iterable[str]:
    if not text:
        return
    start = 0
    while start < len(text):
        end = min(len(text), start + size)
        if end < len(text):
            boundary = text.rfind(". ", start + size // 2, end)
            if boundary > start:
                end = boundary + 1
        yield text[start:end].strip()
        if end >= len(text):
            break
        start = max(start + 1, end - overlap)


def _tokens(text: str) -> list[str]:
    stopwords = {"a", "o", "as", "os", "de", "da", "do", "das", "dos", "e", "em", "para", "por", "com", "um", "uma", "que", "ou", "no", "na"}
    words = [word for word in re.findall(r"[a-zA-ZÀ-ÿ0-9]{2,}", text.lower()) if word not in stopwords]
    return words + [f"{a}_{b}" for a, b in zip(words, words[1:])]


def _embed(text: str, dimensions: int) -> list[float]:
    vector = [0.0] * dimensions
    for token in _tokens(text):
        digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
        value = int.from_bytes(digest, "big")
        index = value % dimensions
        vector[index] += 1.0 if value & 1 else -1.0
    norm = math.sqrt(sum(item * item for item in vector)) or 1.0
    return [round(item / norm, 7) for item in vector]


def _dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def _section(text: str) -> str | None:
    first_sentence = text.split(".", 1)[0].strip()
    return first_sentence[:120] if 3 <= len(first_sentence) <= 120 else None
