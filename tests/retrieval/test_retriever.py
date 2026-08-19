from pathlib import Path

from netops_ingestion.domain.document_chunk import DocumentChunk
from netops_ingestion.embeddings.base import EmbeddingModel
from netops_ingestion.retrieval.retriever import Retriever
from netops_ingestion.vector_store.base import VectorStore


class FakeEmbeddingModel(EmbeddingModel):
    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[1.0, 0.0, 0.0] for _ in texts]


class FakeVectorStore(VectorStore):
    def add(
        self,
        chunks: list[DocumentChunk],
        embeddings: list[list[float]],
    ) -> None:
        pass

    def search(
        self,
        embedding: list[float],
        top_k: int,
    ) -> list[DocumentChunk]:
        return [
            DocumentChunk(
                content="Firewall troubleshooting procedure",
                source=Path("firewall.txt"),
                chunk_index=0,
            )
        ]


def test_retriever_embeds_query_and_searches() -> None:
    embedding_model = FakeEmbeddingModel()
    vector_store = FakeVectorStore()

    retriever = Retriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    results = retriever.retrieve(
        query="How do I troubleshoot firewall connectivity?",
        top_k=3,
    )

    assert len(results) == 1
    assert results[0].content == "Firewall troubleshooting procedure"