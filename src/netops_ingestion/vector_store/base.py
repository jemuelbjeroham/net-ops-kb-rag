from abc import ABC, abstractmethod

from netops_ingestion.domain.document_chunk import DocumentChunk


class VectorStore(ABC):
    """
    Contract for the Vector Store
    """

    @abstractmethod
    def add(self, chunks: list[DocumentChunk], embeddings: list[list[float]]) -> list[DocumentChunk]:
        """
        Store the Embeddings of the chunks and their metadata
        """
        raise NotImplementedError

    @abstractmethod
    def search(self, embedding: list[float], top_k: int) -> list[DocumentChunk]:
        """
        Return the most similar document chunks
        """
        raise NotImplementedError