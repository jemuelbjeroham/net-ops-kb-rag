from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class DocumentChunk:
    """
    Represents the chunk of a document
    """
    content: str
    source: Path
    chunk_index: int
    metadata: dict[str, str] = field(default_factory=dict)