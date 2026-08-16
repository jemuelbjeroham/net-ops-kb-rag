from pathlib import Path

import pytest

from netops_ingestion.chunking.recursive_chunker import RecursiveChunker
from netops_ingestion.domain.document import Document


def test_valid_chunker_configuration() -> None:
    chunker = RecursiveChunker(
        chunk_size=500,
        chunk_overlap=50,
    )

    assert chunker.chunk_size == 500
    assert chunker.chunk_overlap == 50

def test_chunk_size_must_be_greater_than_zero() -> None:
    with pytest.raises(ValueError, match="chunk size"):
        RecursiveChunker(
            chunk_size=0,
            chunk_overlap=0
        )

def test_chunk_overlap_must_not_be_negative() -> None:
    with pytest.raises(ValueError, match="chunk overlap"):
        RecursiveChunker(
            chunk_size=500,
            chunk_overlap=-1,
        )


def test_chunk_overlap_must_be_less_than_chunk_size() -> None:
    with pytest.raises(ValueError, match="chunk overlap"):
        RecursiveChunker(
            chunk_size=500,
            chunk_overlap=500,
        )

def test_document_smaller_than_chunk_size_returns_single_chunk() -> None:
    document = Document(
        content="This is a small document.",
        source=Path("runbook.txt"),
    )

    chunker = RecursiveChunker(
        chunk_size=100,
        chunk_overlap=20,
    )

    chunks = chunker.chunk(document)

    assert len(chunks) == 1
    assert chunks[0].content == document.content
    assert chunks[0].chunk_index == 0
    assert chunks[0].source == document.source