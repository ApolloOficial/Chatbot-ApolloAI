"""Recuperação RAG a partir dos Markdown do corpus solar."""

from __future__ import annotations

import hashlib
import logging
import math
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable

logger = logging.getLogger(__name__)

TASK_13_URL = "https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-systems/"
TASK_12_URL = "https://iea-pvps.org/research-tasks/pv-sustainability/"

SOURCE_URLS = {
    "nrel_pv_om_best_practices_sintese.md": "https://www.nrel.gov/docs/fy17osti/68281.pdf",
    "FS-Climate-Optimisation-2025.pdf": "https://doi.org/10.69766/QSYC8858",
    "IEA-PVPS-T13-2026-FS-Agrivoltaics.pdf": "https://iea-pvps.org/key-topics/dual-land-use-agriculture-solar-power-production/",
    "IEA-PVPS-T13-27-2024.pdf": TASK_13_URL,
    "IEA-PVPS-T13-28-2024-REPORT-Technical-and-Economic-KPIs.pdf": TASK_13_URL,
    "IEA-PVPS-T13-29-2025-REPORT-Dual-Land-Use.pdf": "https://iea-pvps.org/key-topics/dual-land-use-agriculture-solar-power-production/",
    "IEA-PVPS-T13-30-2025-PVFS-ANNEX-Degradation-and-Failure.pdf": TASK_13_URL,
    "IEA-PVPS-T13-30-2025-REPORT-Degradation-and-Failure.pdf": TASK_13_URL,
    "IEA-PVPS-T13-31-2025-REPORT-Floating-PV-Plants.pdf": TASK_13_URL,
    "IEA-PVPS-T13-32-2025-REPORT-Climate-Optimisation-2025.pdf": "https://doi.org/10.69766/QSYC8858",
    "IEA-PVPS-T13-33-2025-REPORT-Extreme-Weather-Impacts.pdf": TASK_13_URL,
    "IEA-PVPS-T13-34-2026-REPORT-Digitalisation-Twins.pdf": "https://iea-pvps.org/key-topics/t13-digitalisation-twins-pv-systems-2026/",
    "IEA-PVPS-T13-35-2026-REPORT-PV-BESS-2026.pdf": TASK_13_URL,
    "IEA-PVPS-T13-36-2026-REPORT-pv-project-decisions.pdf": "https://iea-pvps.org/key-topics/t13-pv-project-decisions-2026/",
    "IEA-PVPS-T13-37-2026-REPORT-Second-Life-PV.pdf": TASK_13_URL,
    "IEA-PVPS-T13-39-2026-REPORT-Optimisation-PV.pdf": TASK_13_URL,
    "IEA-PVPS-T13-40-2026-REPORT-Arctic-PV.pdf": "https://iea-pvps.org/key-topics/t13-security-greater-arctic-region-2026/",
    "IEA_PVPS_T12_Preliminary-EnvEcon-Analysis-of-module-reuse_2021_report.pdf": TASK_12_URL,
    "IEA_PVPS_Task12_Methodological_Guidelines_NEA_2021_report.pdf": TASK_12_URL,
    "IEA_Task12_LCA_Guidelines.pdf": TASK_12_URL,
}

_QUERY_TRANSLATIONS = {
    "agrivoltaico": ("agrivoltaic", "agrivoltaics"),
    "agrivoltaicos": ("agrivoltaic", "agrivoltaics"),
    "avaliar": ("assess", "assessment", "evaluation"),
    "bateria": ("battery", "bess"),
    "baterias": ("batteries", "bess"),
    "clima": ("climate",),
    "confiabilidade": ("reliability",),
    "degradacao": ("degradation",),
    "desempenho": ("performance",),
    "economico": ("economic",),
    "economicos": ("economic",),
    "falha": ("failure", "failures"),
    "falhas": ("failure", "failures"),
    "flutuante": ("floating",),
    "fotovoltaico": ("photovoltaic", "pv"),
    "fotovoltaicos": ("photovoltaic", "pv"),
    "indicadores": ("indicators", "kpi", "kpis"),
    "manutencao": ("maintenance",),
    "modo": ("mode", "modes"),
    "modos": ("mode", "modes"),
    "modulo": ("module", "modules"),
    "modulos": ("module", "modules"),
    "otimizacao": ("optimisation", "optimization"),
    "reuso": ("reuse", "second_life"),
    "seguranca": ("safety",),
    "sombreamento": ("shading", "shaded"),
    "tecnico": ("technical",),
    "tecnicos": ("technical",),
}


class SolarKnowledgeBase:
    """Recuperação dos documentos indexados no Qdrant remoto."""

    def __init__(self, documents_dir: Path, top_k: int = 5, semantic_store=None):
        self.documents_dir = Path(documents_dir)
        self.top_k = top_k
        self.semantic_store = semantic_store

    @classmethod
    def from_config(cls, config):
        from app.qdrant_store import QdrantSemanticStore

        return cls(config["SOLAR_DOCUMENTS_DIR"], config["RAG_TOP_K"], QdrantSemanticStore.from_config(config))

    @property
    def is_ready(self) -> bool:
        return bool(self.semantic_store and self.semantic_store.is_ready())

    def index_qdrant(self, vector_store, batch_size: int = 50, on_progress=None) -> int:
        """Lê os Markdown atuais e envia seus chunks ao Qdrant em lotes."""
        if batch_size < 1:
            raise ValueError("QDRANT_INDEX_BATCH_SIZE deve ser maior que zero.")
        paths = self._document_paths(require_complete=True)
        if not paths:
            raise ValueError("Nenhum Markdown encontrado para indexação no Qdrant.")
        chunks = [chunk for path in paths for chunk in self._extract_text(path)]
        if not chunks:
            raise ValueError("Os arquivos Markdown não produziram trechos para indexar.")
        vector_store.ensure_collections()
        vector_store.require_empty_collections()
        for start in range(0, len(chunks), batch_size):
            vector_store.upsert_document_chunks(chunks[start:start + batch_size])
            if on_progress:
                on_progress(min(start + batch_size, len(chunks)), len(chunks))
        logger.info("rag_qdrant_indexado", extra={"chunks": len(chunks)})
        return len(chunks)

    def _document_paths(self, require_complete: bool = False) -> list[Path]:
        if not self.documents_dir.is_dir():
            return []
        markdown_dir = self.documents_dir / "markdown"
        if require_complete:
            missing = [path.name for path in self.documents_dir.glob("*.pdf")
                       if not (markdown_dir / f"{path.stem}.md").is_file()]
            if missing:
                raise ValueError(f"Converta os PDFs para Markdown antes de indexar: {', '.join(sorted(missing))}")
        return sorted(self.documents_dir.glob("*.md")) + sorted(markdown_dir.glob("*.md"))

    def _extract_text(self, path: Path) -> list[dict[str, Any]]:
        text = path.read_text(encoding="utf-8")
        source_pdf = self.documents_dir / f"{path.stem}.pdf"
        converted = path.parent == self.documents_dir / "markdown" and source_pdf.is_file()
        document_name = source_pdf.name if converted else path.name
        if converted:
            parts = re.split(r"(?m)^## Página (\d+)\s*$", text)
            if len(parts) < 3:
                raise ValueError(f"Markdown convertido sem páginas: {path.name}")
            pages = ((int(number), content) for number, content in zip(parts[1::2], parts[2::2]))
        else:
            pages = ((None, text),)
        result = []
        for page_number, content in pages:
            for part_number, part in enumerate(_split(_clean(content)), 1):
                chunk = {
                    "id": f"{path.stem}-p{page_number}-c{part_number}" if page_number else f"{path.stem}-c{part_number}",
                    "documento": document_name, "pagina": page_number,
                    "secao": _section(part), "url": SOURCE_URLS.get(document_name), "trecho": part,
                }
                result.append(chunk)
        return result

    def retrieve(self, query: str, route: str = "ativos_solares") -> list[dict[str, Any]]:
        del route
        if not self.semantic_store or not self.semantic_store.configured:
            from app.qdrant_store import QdrantUnavailable

            raise QdrantUnavailable("Qdrant remoto não configurado.")
        return self.semantic_store.search_document_chunks(query, self.top_k)


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
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    normalized = "".join(char for char in decomposed if not unicodedata.combining(char))
    words = [word for word in re.findall(r"[a-z0-9]{2,}", normalized) if word not in stopwords]
    return words + [f"{a}_{b}" for a, b in zip(words, words[1:])]


def _query_tokens(text: str) -> list[str]:
    tokens = _tokens(text)
    expanded = list(tokens)
    for token in tokens:
        expanded.extend(_QUERY_TRANSLATIONS.get(token, ()))
    return expanded


def _embed(text: str, dimensions: int) -> list[list[int | float]]:
    return _embed_tokens(_tokens(text), dimensions)


def _embed_tokens(tokens: list[str], dimensions: int) -> list[list[int | float]]:
    vector: dict[int, float] = {}
    for token in tokens:
        digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
        value = int.from_bytes(digest, "big")
        index = value % dimensions
        vector[index] = vector.get(index, 0.0) + (1.0 if value & 1 else -1.0)
    vector = {index: value for index, value in vector.items() if value}
    norm = math.sqrt(sum(item * item for item in vector.values())) or 1.0
    return [[index, round(value / norm, 7)] for index, value in sorted(vector.items())]


def _section(text: str) -> str | None:
    first_sentence = text.split(".", 1)[0].strip()
    return first_sentence[:120] if 3 <= len(first_sentence) <= 120 else None
