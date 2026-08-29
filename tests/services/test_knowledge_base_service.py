from pathlib import Path

from netops_ingestion.domain.document_chunk import DocumentChunk
from netops_ingestion.services.knowledge_base_service import KnowledgeBaseService


class FakeRetriever:
    def retrieve(self, query: str, top_k: int) -> list[DocumentChunk]:
        return [
            DocumentChunk(
                content="Firewall troubleshooting procedure",
                source=Path("firewall.txt"),
                chunk_index=0,
            )
        ]

def test_knowledge_base_service_search() -> None:
    service = KnowledgeBaseService(retriever=FakeRetriever())
    results = service.search(query="How do I troubleshoot firewall connectivity?", top_k=5)
    assert len(results) == 1
    assert results[0].content == "Firewall troubleshooting procedure"