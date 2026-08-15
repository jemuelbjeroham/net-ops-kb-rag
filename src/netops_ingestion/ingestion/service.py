
from pathlib import Path

from netops_ingestion.domain.document import Document
from netops_ingestion.loaders.factory import LoaderFactory


class IngestionService:

    def ingest(self, source: Path) -> list[Document]:
        loader = LoaderFactory.create(source)

        return loader.load()