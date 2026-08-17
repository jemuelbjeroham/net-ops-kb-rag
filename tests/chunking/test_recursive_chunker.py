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


def test_oversized_document_is_split_into_multiple_chunks() -> None:
    document = Document(
        content=(
            "Firewall policy configuration is required before implementing the change.\n\n"
            "The engineer must verify the source, destination, ports, and protocol "
            "before applying the policy."
        ),
        source=Path("runbook.txt"),
    )

    chunker = RecursiveChunker(
        chunk_size=100,
        chunk_overlap=20,
    )

    chunks = chunker.chunk(document)

    assert len(chunks) == 2

    assert chunks[0].content == (
        "Firewall policy configuration is required before implementing the change."
    )

    assert chunks[1].content == (
        "The engineer must verify the source, destination, ports, and protocol "
        "before applying the policy."
    )

    assert chunks[0].chunk_index == 0
    assert chunks[1].chunk_index == 1


def test_oversized_paragraph_is_split_further() -> None:
    document = Document(
        content=(
            "The firewall administrator must verify the source address, "
            "destination address, protocol, and destination port before "
            "applying the firewall policy."
        ),
        source=Path("runbook.txt"),
    )

    chunker = RecursiveChunker(
        chunk_size=50,
        chunk_overlap=10,
    )

    chunks = chunker.chunk(document)

    assert len(chunks) > 1


def test_split_text_splits_using_separator() -> None:
    chunker = RecursiveChunker(
        chunk_size=100,
        chunk_overlap=20,
    )

    text = "First paragraph\n\nSecond paragraph"

    result = chunker._split_text(text, ["\n\n", "\n", " ", ""])

    assert result == [
        "First paragraph",
        "Second paragraph",
    ]


def test_split_text_uses_next_separator_when_first_is_insufficient() -> None:
    chunker = RecursiveChunker(
        chunk_size=31,
        chunk_overlap=5,
    )

    text = (
        "First line contains some text.\n"
        "Second line contains some text."
    )

    result = chunker._split_text(
        text,
        ["\n\n", "\n", " ", ""],
    )

    assert result == [
        "First line contains some text.",
        "Second line contains some text.",
    ]


def test_merge_parts_respects_chunk_size() -> None:
    chunker = RecursiveChunker(
        chunk_size=20,
        chunk_overlap=5,
    )

    parts = ["The", "firewall", "administrator"]

    result = chunker._merge_parts(parts, " ")

    assert result == [
        "The firewall",
        "administrator",
    ]