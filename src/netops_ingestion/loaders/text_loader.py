from netops_ingestion.domain.document import Document
from netops_ingestion.loaders.base import BaseLoader


class TextLoader(BaseLoader):
    """
    This is a Loader for document of Text types
    """

    def load(self) -> list[Document]:
        content = self.source.read_text(encoding="utf-8")
        document = Document(
            content=content,
            source=self.source,
            metadata={
                "loader": "TextLoader",
                "file_type": self.source.suffix.lstrip("."),
            },
        )
        return [document]

