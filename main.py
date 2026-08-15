from pathlib import Path

from netops_ingestion.ingestion.service import IngestionService


def main() -> None:

    service = IngestionService()
    documents = service.ingest(Path("sample_data/firewall_operations.pdf"))
    print(documents)



if __name__ == "__main__":
    main()
