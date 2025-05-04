# rebuild_index.py

from backend.embeddings import create_vector_store

if __name__ == "__main__":
    create_vector_store()
    print("✅ New FAISS index created from updated knowledge.txt")
