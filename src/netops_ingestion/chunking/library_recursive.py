from langchain_text_splitters import RecursiveCharacterTextSplitter

from netops_ingestion.domain.document import Document
from netops_ingestion.domain.document_chunk import DocumentChunk


class LibraryRecursiveChunker:
    """
    Uses the Langchain's RecursiveCharacterTextSplitter
    to split documents into chunks
    """
    def __init__(self, chunk_size: int, chunk_overlap: int) -> None:
        self._splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def chunk(self, document: Document) -> list[DocumentChunk]:
        text_chunks = self._splitter.split_text(document.content)

        return [
            DocumentChunk(
                content=text,
                source=document.source,
                chunk_index=index,
                metadata=document.metadata.copy(),
            )
            for index, text in enumerate(text_chunks)
        ]