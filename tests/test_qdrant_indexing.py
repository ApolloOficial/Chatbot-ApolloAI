from app.config import Config
from app.services.rag import SolarKnowledgeBase


class RecordingStore:
    def __init__(self):
        self.ready = False
        self.count = 0
        self.documents = set()

    def ensure_collections(self):
        self.ready = True

    def require_empty_collections(self):
        assert self.ready

    def upsert_document_chunks(self, chunks):
        assert self.ready
        self.count += len(chunks)
        self.documents.update(chunk["documento"] for chunk in chunks)
        assert all(chunk["trecho"] != "stale index" for chunk in chunks)
        assert all("embedding" not in chunk and "termos" not in chunk for chunk in chunks)


def test_qdrant_indexing_reads_current_markdowns_instead_of_cached_index():
    knowledge = SolarKnowledgeBase.from_config(Config.__dict__)
    store = RecordingStore()

    total = knowledge.index_qdrant(store, batch_size=200)

    assert total == store.count
    assert total > 0
    assert "IEA-PVPS-T13-30-2025-REPORT-Degradation-and-Failure.pdf" in store.documents
    assert "nrel_pv_om_best_practices_sintese.md" in store.documents
