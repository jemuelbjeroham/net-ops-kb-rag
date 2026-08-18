import torch
from sentence_transformers import SentenceTransformer

from netops_ingestion.embeddings.base import EmbeddingModel


class SentenceTransformerEmbedding(EmbeddingModel):
    """
    Embedding model backed by the Sentence Transformers
    """

    def __init__(self, model_name: str) -> None:
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.model = SentenceTransformer(model_name, device=device)

    def embed(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
        )

        return embeddings.tolist()

