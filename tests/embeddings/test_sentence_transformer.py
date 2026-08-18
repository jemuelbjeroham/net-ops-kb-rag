# import time

from netops_ingestion.embeddings.sentence_transformer import (
    SentenceTransformerEmbedding,
)


def test_qwen_embedding_model() -> None:
    # start = time.perf_counter()
    model = SentenceTransformerEmbedding("Qwen/Qwen3-Embedding-0.6B")
    # print(f"\nModel Initialization: { time.perf_counter() - start:.2f}s")
    # print(f"Device: {model.model.device}")

    # start = time.perf_counter()
    embeddings = model.embed(
        [
            "How to restart a cisco router and a paloalto firewall",
            "How do I troubleshoot firewall connectivity?",
        ]
    )
    # print(f"Embeddding Inference: {time.perf_counter() - start:.2f}s")

    assert len(embeddings) == 2
    assert len(embeddings[0]) == 1024
    assert len(embeddings[1]) == 1024

