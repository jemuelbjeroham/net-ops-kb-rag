from abc import ABC, abstractmethod
from pathlib import Path

from netops_ingestion.domain.document import Document


class BaseLoader(ABC):
    """
    Base contract for loaders of all document types
    """

    def __init__(self, source: Path) -> None:
        self.source = source
        
    @abstractmethod
    def load(self) -> list[Document]:
        """
        Load one or more documents from a source
        """
        raise NotImplementedError