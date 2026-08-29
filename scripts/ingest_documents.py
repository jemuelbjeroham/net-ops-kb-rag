from pathlib import Path

from netops_ingestion.loaders.factory import LoaderFactory


def main() -> None:
    documents = []

    for source in sorted(Path("sample_data").iterdir()):
        if not source.is_file():
            continue

        loader = LoaderFactory.create(source)
        documents.extend(loader.load())

    print(f"Loaded {len(documents)} documents")

if __name__ == "__main__":
    main()
    