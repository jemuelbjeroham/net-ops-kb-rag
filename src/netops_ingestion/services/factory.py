from netops_ingestion.embeddings.sentence_transformer import (
    SentenceTransformerEmbedding,
)
from netops_ingestion.retrieval.retriever import Retriever
from netops_ingestion.services.knowledge_base_service import KnowledgeBaseService
from netops_ingestion.vector_store.chroma_store import ChromaVectorStore


def create_knowledge_base_service(embedding_model: str, collection_name: str, persist_directory: str) -> KnowledgeBaseService:
    embedding = SentenceTransformerEmbedding(model_name=embedding_model)
    vector_store = ChromaVectorStore(collection_name=collection_name, persist_directory=persist_directory)

    retriever = Retriever(embedding_model=embedding, vector_store=vector_store)

    return KnowledgeBaseService(retriever=retriever)