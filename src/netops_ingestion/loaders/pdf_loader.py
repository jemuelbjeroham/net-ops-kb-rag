
import pymupdf

from netops_ingestion.domain.document import Document
from netops_ingestion.loaders.base import BaseLoader


class PDFLoader(BaseLoader):
    """
    Loads PDF documents into Document objects.
    """
    def load(self) -> list[Document]:
        documents = []
        with pymupdf.open(self.source) as pdf:
            for page in pdf:
                text = page.get_text("text")

                if not text.strip():
                    continue

                document = Document(
                    content=text,
                    source=self.source,
                    metadata={
                        "loader": "PDFLoader",
                        "file_type": self.source.suffix.lstrip("."),
                        "page_number": page.number + 1,
                    },      
                )
                documents.append(document)

        return documents
