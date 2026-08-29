import chromadb


def main() -> None:
    client = chromadb.PersistentClient(path="storage/chroma")
    collection = client.get_collection(name="netops_kb")

    print(f"Collection: {collection.name}")
    print(f"Record count: {collection.count()}")

if __name__ == "__main__":
    main()