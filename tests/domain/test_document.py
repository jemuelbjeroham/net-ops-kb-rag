from pathlib import Path

from netops_ingestion.domain.document import Document


def test_document_creation() -> None:
    source = Path("runbook.txt")

    document = Document(
        content="Allow HTTPS traffic to firewall.",
        source=source,
    )

    assert document.content == "Allow HTTPS traffic to firewall."
    assert document.source == source