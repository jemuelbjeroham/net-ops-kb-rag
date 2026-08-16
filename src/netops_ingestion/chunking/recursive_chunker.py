from netops_ingestion.domain.document import Document
from netops_ingestion.domain.document_chunk import DocumentChunk


class RecursiveChunker:
    """
    Splits the documents into smaller chunks based on the recusive separators
    """
    def __init__(self, chunk_size: int, chunk_overlap:int) -> None:
        if chunk_size <= 0:
            raise ValueError(f"Invalid chunk size: {chunk_size}. Value must be greater than 0.")
        if chunk_overlap < 0:
            raise ValueError(f"Invalid chunk overlap: {chunk_overlap}. Value must not be negative")
        if chunk_overlap >= chunk_size:
            raise ValueError(f"Invalid chunk overlap: {chunk_overlap} must be less than chunk size {chunk_size}")

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, document: Document) -> list[DocumentChunk]:
        chunk = Document(
            content=document.content,
            source=document.source,
            chunk_index=0,
            metadata=document.metadata.copy(),
        )

        return [chunk]