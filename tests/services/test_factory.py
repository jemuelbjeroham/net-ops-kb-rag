from unittest.mock import patch

from netops_ingestion.services.factory import create_knowledge_base_service
from netops_ingestion.services.knowledge_base_service import KnowledgeBaseService


def test_create_knowledge_base_service() -> None:
    with (
        patch(
            "netops_ingestion.services.factory.SentenceTransformerEmbedding"
        ) as embedding_class,
        patch(
            "netops_ingestion.services.factory.ChromaVectorStore"
        ) as vector_store_class,
    ):
        service = create_knowledge_base_service(
            embedding_model="test-model",
            collection_name="test_collection",
            persist_directory="test_storage",
        )

    assert isinstance(service, KnowledgeBaseService)

    embedding_class.assert_called_once_with(
        model_name="test-model",
    )

    vector_store_class.assert_called_once_with(
        collection_name="test_collection",
        persist_directory="test_storage",
    )