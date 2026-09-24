from pathlib import Path

import pytest
from pypdf import PdfWriter

from app.services.rag import SolarKnowledgeBase
from scripts.convert_pdfs_to_markdown import convert_pdf


def test_converter_marks_pages_and_indexer_prefers_markdown(workspace_tmp_path: Path):
    documents = workspace_tmp_path / "documentos"
    documents.mkdir()
    pdf = documents / "technical-guide.pdf"
    writer = PdfWriter()
    writer.add_blank_page(width=100, height=100)
    with pdf.open("wb") as stream:
        writer.write(stream)

    knowledge = SolarKnowledgeBase(documents)
    class RecordingStore:
        def __init__(self):
            self.chunks = []
        def ensure_collections(self):
            pass
        def require_empty_collections(self):
            pass
        def upsert_document_chunks(self, chunks):
            self.chunks.extend(chunks)
    store = RecordingStore()
    with pytest.raises(ValueError, match="Converta os PDFs"):
        knowledge.index_qdrant(store)

    markdown, page_count, empty_count = convert_pdf(pdf, documents / "markdown")
    assert page_count == empty_count == 1
    assert "## Página 1" in markdown.read_text(encoding="utf-8")

    markdown.write_text("# Guide\n\n## Página 1\n\nPhotovoltaic module maintenance.\n", encoding="utf-8")
    assert knowledge._document_paths() == [markdown]
    assert knowledge.index_qdrant(store) == 1
    source = store.chunks[0]
    assert source["documento"] == pdf.name
    assert source["pagina"] == 1
