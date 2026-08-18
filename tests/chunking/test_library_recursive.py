from pathlib import Path

from netops_ingestion.chunking.library_recursive import LibraryRecursiveChunker
from netops_ingestion.domain.document import Document


def test_library_recursive_chunker_creates_chunks() -> None:
    document = Document(
        content=(
            "Firewall policy configuration must be verified before implementation. "
            "The engineer must check the source and destination addresses. "
            "The engineer must also verify the protocol and destination port."            
        ),
        source=Path("runbook.txt"),   
    )

    chunker = LibraryRecursiveChunker(
        chunk_size=50,
        chunk_overlap=10,
    )

    chunks = chunker.chunk(document)

    assert len(chunks) > 1
    assert chunks[0].chunk_index == 0
    assert chunks[0].source == document.source
    assert chunks[0].metadata == document.metadata

    assert all(len(chunk.content) <= 50 for chunk in chunks)