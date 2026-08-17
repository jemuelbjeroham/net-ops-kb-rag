from netops_ingestion.domain.document import Document
from netops_ingestion.domain.document_chunk import DocumentChunk


class RecursiveChunker:
    """
    Splits the documents into smaller chunks based on the recusive separators
    """
    def __init__(self, chunk_size: int, chunk_overlap:int) -> None:
        if chunk_size <= 0:
            raise ValueError(f"Invalid chunk size: {chunk_size}. Value must be greater than 0.")
        if chunk_overlap < 0:
            raise ValueError(f"Invalid chunk overlap: {chunk_overlap}. Value must not be negative")
        if chunk_overlap >= chunk_size:
            raise ValueError(f"Invalid chunk overlap: {chunk_overlap} must be less than chunk size {chunk_size}")

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, document: Document) -> list[DocumentChunk]:
        separators = ["\n\n", "\n", " ", ""]

        text_chunks = self._split_recursive(document.content, separators)

        return [
            DocumentChunk(
                content=text,
                source=document.source,
                chunk_index=index,
                metadata=document.metadata.copy()
            )
            for index, text in enumerate(text_chunks)
        ]


    def _split_by_separator(self, text: str, separator: str) -> list[str]:
        return text.split(separator)


    def _merge_parts(self, parts: list[str], separator: str) -> list[str]:
        chunks = []
        current_chunk = ""

        for part in parts:
            if not current_chunk:
                current_chunk = part
                continue

            candidate = current_chunk + separator + part

            if len(candidate) <= self.chunk_size:
                current_chunk = candidate
            else:
                chunks.append(current_chunk)
                current_chunk = part

        if current_chunk:
            chunks.append(current_chunk)

        return chunks


    def _split_recursive(self, text: str, separators: list[str]) -> list[str]:
        if len(text) <= self.chunk_size:
            return [text]

        if not separators:
            return [text]

        separator = separators[0]

        if separator == "":
            return [
                text[i:i + self.chunk_size]
                for i in range(0, len(text), self.chunk_size)
            ]

        parts = self._split_by_separator(text, separator)

        merged = self._merge_parts(parts, separator)

        result = []

        for chunk in merged:
            if len(chunk) <= self.chunk_size:
                result.append(chunk)
            else:
                result.extend(
                    self._split_recursive(chunk, separators[1:])
                )

        return result