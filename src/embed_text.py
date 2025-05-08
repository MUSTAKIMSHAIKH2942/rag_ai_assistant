# from sentence_transformers import SentenceTransformer

# def get_embedding_model():
#     # Using a more recent model that works well
#     return SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# def embed_text(text):
#     model = get_embedding_model()
#     # Split text into chunks (better than simple split("\n"))
#     sentences = [text[i:i+512] for i in range(0, len(text), 512)]
#     embeddings = model.encode(sentences)
#     return sentences, embeddings, model  # Return model for later use

# embed_text.py
from sentence_transformers import SentenceTransformer

def get_embedding_model():
    # Using a model that's optimized for sentence-level embeddings
    return SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def embed_text(chunks):
    model = get_embedding_model()
    embeddings = model.encode(chunks)
    return chunks, embeddings, model  # Return model for later use
