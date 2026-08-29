from pathlib import Path

from netops_ingestion.loaders.factory import LoaderFactory


def main() -> None:
    source = Path("sample_data/firewall_operations_runbook.pdf")

    documents = LoaderFactory.create(source).load()

    for document in documents:
        print("---")
        print(f"Source: {document.source}")
        print(f"Metadata: {document.metadata}")
        print(f"Content: {document.content[:100]}")


if __name__ == "__main__":
    main()