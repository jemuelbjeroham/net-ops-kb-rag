from netops_ingestion.domain.document_chunk import DocumentChunk
from netops_ingestion.retrieval.retriever import Retriever


class KnowledgeBaseService:
    """
    Application-facing interface for querying the VectorStore
    """
    def __init__(self, retriever: Retriever) -> None:
        self.retriever = retriever

    def search(self, query: str, top_k: int = 5) -> list[DocumentChunk]:
        return self.retriever.retrieve(query=query, top_k=top_k)
