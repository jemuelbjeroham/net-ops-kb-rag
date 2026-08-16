from pathlib import Path

from netops_ingestion.domain.document_chunk import DocumentChunk


def test_document_chunk_creation() -> None:
    source = Path("runbook.txt")

    chunk = DocumentChunk(
        content="Sample Chunk Text",
        source=source,
        chunk_index=0,
    )

    assert chunk.content == "Sample Chunk Text"
    assert chunk.source == source
    assert chunk.chunk_index == 0
    assert chunk.metadata == {}