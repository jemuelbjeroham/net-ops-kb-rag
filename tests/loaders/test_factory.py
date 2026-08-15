from pathlib import Path

import pytest

from netops_ingestion.loaders.factory import LoaderFactory, PDFLoader, TextLoader


def test_factory_creates_text_loader() -> None:
    loader = LoaderFactory.create(Path("runbook.txt"))

    assert isinstance(loader, TextLoader)


def test_factory_creates_pdf_loader() -> None:
    loader = LoaderFactory.create(Path("runbook.pdf"))

    assert isinstance(loader, PDFLoader)

def test_factory_rejects_unsupported_file_type() -> None:
    with pytest.raises(ValueError, match="Unsupported file type"):
        LoaderFactory.create(Path("network.vsdx"))