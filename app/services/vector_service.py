import chromadb
from sentence_transformers import SentenceTransformer


class VectorService:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="aec_documents"
        )

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def store_chunks(
        self,
        chunks: list[str],
        filename: str
    ) -> int:

        embeddings = self.embedding_model.encode(
            chunks
        ).tolist()

        ids = [
            f"{filename}_{index}"
            for index in range(len(chunks))
        ]

        metadatas = [
            {
                "filename": filename,
                "chunk_index": index
            }
            for index in range(len(chunks))
        ]

        self.collection.upsert(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

        return len(chunks)