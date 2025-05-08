# from .extract_text import extract_text_from_pdf
# from .embed_text import embed_text
# from .faiss_index import create_faiss_index, query_faiss
# from .generate_answer import generate_answer

# def run_rag_system(pdf_path, query):
#     # Extract text
#     pdf_text = extract_text_from_pdf(pdf_path)
    
#     # Embed text and get model
#     sentences, embeddings, model = embed_text(pdf_text)
    
#     # Create index
#     index = create_faiss_index(embeddings)
    
#     # Query index
#     indices, distances = query_faiss(index, query, model)
    
#     # Retrieve relevant text
#     retrieved_text = " ".join([sentences[i] for i in indices[0]])
    
#     # Generate answer
#     answer = generate_answer(retrieved_text, query)
    
#     return answer

# rag_system.py
from .extract_text import extract_text_from_pdf
from .embed_text import embed_text
from .faiss_index import create_faiss_index, query_faiss
from .generate_answer import generate_answer

def run_rag_system(pdf_path, query):
    # Extract text
    chunks = extract_text_from_pdf(pdf_path)
    
    # Embed text and get model
    sentences, embeddings, model = embed_text(chunks)
    
    # Create FAISS index
    index = create_faiss_index(embeddings)
    
    # Query the index
    indices, distances = query_faiss(index, query, model)
    
    # Retrieve relevant text from the most similar chunks
    retrieved_text = " ".join([sentences[i] for i in indices[0]])
    
    # Generate the final answer
    answer = generate_answer(retrieved_text, query)
    
    return answer
