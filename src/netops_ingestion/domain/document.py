from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Document:
    """
    Represents a document related to NetOps
    """
    content: str
    source: Path
    metadata: dict[str, str] = field(default_factory=dict)