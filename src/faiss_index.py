# import faiss
# import numpy as np

# def create_faiss_index(embeddings):
#     embedding_matrix = np.array(embeddings).astype("float32")
#     index = faiss.IndexFlatL2(embedding_matrix.shape[1])
#     index.add(embedding_matrix)
#     return index

# def query_faiss(index, query, model, top_k=5):
#     query_embedding = model.encode([query])
#     query_embedding = np.array(query_embedding).astype("float32")
#     distances, indices = index.search(query_embedding, top_k)
#     return indices, distances


# faiss_index.py
import faiss
import numpy as np

def create_faiss_index(embeddings):
    embedding_matrix = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embedding_matrix.shape[1])
    index.add(embedding_matrix)
    return index

def query_faiss(index, query, model, top_k=5):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    return indices, distances
