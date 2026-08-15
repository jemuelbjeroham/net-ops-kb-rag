from pathlib import Path

from netops_ingestion.loaders.pdf_loader import PDFLoader

# def main() -> None:

#     service = IngestionService()
#     documents = service.ingest(Path("sample_data/firewall_runbook.txt"))
#     print(documents)

def main() -> None:
    loader = PDFLoader(
        Path("sample_data/firewall_operations.pdf")
    )

    documents = loader.load()

    for document in documents:
        print(f"Source: {document.source}")
        print(f"Page: {document.metadata['page_number']}")
        print(f"Content: {document.content[:80]}")
        print("-" * 50)


if __name__ == "__main__":
    main()
