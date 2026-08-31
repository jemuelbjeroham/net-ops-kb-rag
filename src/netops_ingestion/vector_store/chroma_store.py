from pathlib import Path

import chromadb

from netops_ingestion.domain.document_chunk import DocumentChunk
from netops_ingestion.vector_store.base import VectorStore


class ChromaVectorStore(VectorStore):
    """
    Chroma-backend Vector Store
    """

    def __init__(self, collection_name: str, persist_directory: str) -> None:
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add(self, chunks: list[DocumentChunk], embeddings: list[list[float]]) -> None:
        if len(chunks) != len(embeddings):
            raise ValueError("Number of chunks must match number of the embeddings")

        ids = [self._create_id(chunk) for chunk in chunks]

        documents = [chunk.content for chunk in chunks]
        metadatas = [
            {
                **chunk.metadata,
                "source": str(chunk.source),
                "chunk_index": chunk.chunk_index,
            }
            for chunk in chunks
        ]

        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, embedding: list[float], top_k: int) -> list[DocumentChunk]:
        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        documents = result["documents"][0]
        metadatas = result["metadatas"][0]

        chunks = []

        for document, metadata in zip(
            documents,
            metadatas,
        ):
            chunks.append(
                DocumentChunk(
                    content=document,
                    source=Path(metadata["source"]),
                    chunk_index=int(metadata["chunk_index"]),
                    metadata=metadata,
                )
            )

        return chunks

    def _create_id(self, chunk: DocumentChunk) -> str:
        page_number = chunk.metadata.get("page_number")

        if page_number is not None:
            return (
                f"{chunk.source}:"
                f"page-{page_number}:"
                f"chunk-{chunk.chunk_index}"
            )

        return f"{chunk.source}:chunk-{chunk.chunk_index}"