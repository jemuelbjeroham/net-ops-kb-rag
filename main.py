from netops_ingestion.domain.document import Document


def main() -> None:

    document = Document(content="Allow HTTPs traffic to firewall")

    print(document)

if __name__ == "__main__":
    main()
