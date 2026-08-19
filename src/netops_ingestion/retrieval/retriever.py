from netops_ingestion.domain.document_chunk import DocumentChunk
from netops_ingestion.embeddings.base import EmbeddingModel
from netops_ingestion.vector_store.base import VectorStore


class Retriever:
    """
    Retrieves the most relevant document chunks for a query
    """

    def __init__(self, embedding_model: EmbeddingModel, vector_store: VectorStore) -> None:
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int) -> list[DocumentChunk]:
        query_embedding = self.embedding_model.embed([query])[0]

        return self.vector_store.search(embedding=query_embedding, top_k=top_k)