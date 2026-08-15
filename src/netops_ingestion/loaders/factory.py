from pathlib import Path

from netops_ingestion.loaders.base import BaseLoader
from netops_ingestion.loaders.pdf_loader import PDFLoader
from netops_ingestion.loaders.text_loader import TextLoader


class LoaderFactory:

    @staticmethod
    def create(source: Path) -> BaseLoader:
        suffix = source.suffix.lower().lstrip(".")

        if suffix == "pdf":
            return PDFLoader(source)
        if suffix == "txt":
            return TextLoader(source)

        raise ValueError("Unsupported file type: ", suffix)
