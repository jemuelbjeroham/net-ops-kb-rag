from pathlib import Path

from netops_ingestion.domain.document_chunk import DocumentChunk
from netops_ingestion.vector_store.chroma_store import ChromaVectorStore


def test_chroma_store_add_and_search(tmp_path: Path) -> None:
    store = ChromaVectorStore(
        collection_name="test_collection",
        persist_directory=str(tmp_path),
    )

    chunks = [
        DocumentChunk(
            content="How to troubleshoot firewall connectivity.",
            source=Path("firewall.txt"),
            chunk_index=0,
            metadata={"loader": "test"},
        ),
        DocumentChunk(
            content="How to restart MediaProxy.",
            source=Path("mediaproxy.txt"),
            chunk_index=0,
            metadata={"loader": "test"},
        ),
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    store.add(chunks, embeddings)

    results = store.search(
        embedding=[1.0, 0.0, 0.0],
        top_k=1,
    )

    assert len(results) == 1
    assert results[0].content == (
        "How to troubleshoot firewall connectivity."
    )