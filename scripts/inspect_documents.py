from pathlib import Path

from netops_ingestion.loaders.factory import LoaderFactory


def main() -> None:
    for source in sorted(Path("sample_data").iterdir()):
        if not source.is_file():
            continue

        documents = LoaderFactory.create(source).load()

        print("=" * 80)
        print(f"Source: {source}")
        print(f"Documents: {len(documents)}")

        for document in documents:
            print("-" * 80)
            print(f"Metadata: {document.metadata}")
            print(f"Content preview: {document.content[:150]}")


if __name__ == "__main__":
    main()