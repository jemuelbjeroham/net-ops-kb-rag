import pytest

from netops_ingestion.embeddings.base import EmbeddingModel


def test_embedding_model_is_abstract() -> None:
    with pytest.raises(TypeError):
        EmbeddingModel()

class FakeEmbeddingModel(EmbeddingModel):
    def embed(self, texts: list[str]) -> list[list[float]]:
        return [[0.1, 0.2] for _ in texts]

def test_embedding_model_can_be_implemented() -> None:
    model = FakeEmbeddingModel()

    result = model.embed(["hello", "world"])

    assert result == [
        [0.1, 0.2],
        [0.1, 0.2]
    ]