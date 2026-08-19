from pathlib import Path

from netops_ingestion.domain.document_chunk import DocumentChunk
from netops_ingestion.embeddings.sentence_transformer import (
    SentenceTransformerEmbedding,
)
from netops_ingestion.retrieval.retriever import Retriever
from netops_ingestion.vector_store.chroma_store import ChromaVectorStore


def test_retriever_returns_semantically_relevant_chunk(
    tmp_path: Path,
) -> None:
    chunks = [
        DocumentChunk(
            content=(
                "When firewall connectivity fails, verify the source "
                "address, destination address, protocol, and destination port."
            ),
            source=Path("firewall_runbook.txt"),
            chunk_index=0,
            metadata={"loader": "test"},
        ),
        DocumentChunk(
            content=(
                "When MediaProxy has issues, check the process status "
                "and verify the stream health."
            ),
            source=Path("mediaproxy_runbook.txt"),
            chunk_index=0,
            metadata={"loader": "test"},
        ),
    ]

    embedding_model = SentenceTransformerEmbedding(
        "Qwen/Qwen3-Embedding-0.6B"
    )

    embeddings = embedding_model.embed(
        [chunk.content for chunk in chunks]
    )

    vector_store = ChromaVectorStore(
        collection_name="retrieval_test",
        persist_directory=str(tmp_path),
    )

    vector_store.add(
        chunks=chunks,
        embeddings=embeddings,
    )

    retriever = Retriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    results = retriever.retrieve(
        query="How do I troubleshoot firewall connectivity?",
        top_k=1,
    )

    assert len(results) == 1
    assert results[0].source == Path("firewall_runbook.txt")