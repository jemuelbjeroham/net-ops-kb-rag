from pathlib import Path

from netops_ingestion.chunking.library_recursive import LibraryRecursiveChunker
from netops_ingestion.loaders.factory import LoaderFactory


def main() -> None:
    documents = []

    for source in sorted(Path("sample_data").iterdir()):
        if not source.is_file():
            continue

        loader = LoaderFactory.create(source)
        documents.extend(loader.load())

    print(f"Loaded {len(documents)} documents")

    chunker = LibraryRecursiveChunker(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = []

    for document in documents:
        chunks.extend(chunker.chunk(document))

    print(f"Created {len(chunks)} chunks")

    # for chunk in chunks:
    #     if chunk.metadata.get("file_type") == "pdf":
    #         print("--- PDF CHUNK ---")
    #         print(f"Chunk index: {chunk.chunk_index}")
    #         print(f"Metadata: {chunk.metadata}")
    #         print(f"Content: {chunk.content[:100]}")

if __name__ == "__main__":
    main()
