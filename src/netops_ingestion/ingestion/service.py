
from pathlib import Path

from netops_ingestion.domain.document import Document
from netops_ingestion.loaders.text_loader import TextLoader


class IngestionService:

    def ingest(self, source: Path) -> list[Document]:
        loader = TextLoader(source)

        return loader.load()