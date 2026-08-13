from netops_ingestion.domain.document import Document


def test_document_creation() -> None:
    document = Document(content="Allow HTTPs traffic to firewall")
    assert document.content == "Allow HTTPs traffic to firewall"