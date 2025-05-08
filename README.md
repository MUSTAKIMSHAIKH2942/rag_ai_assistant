# 🤖 RAG AI Assistant (Free & Local)

A lightweight Retrieval-Augmented Generation (RAG) assistant built with **Streamlit, LangChain, FAISS, and Ollama (Mistral model)**. Designed for querying internal company documents (PDFs) with privacy — fully offline, free, and fast.

---

## 🧠 Step-by-Step Setup

### 1️⃣ Install Ollama + Mistral LLM

> Ollama lets you run local LLMs like Mistral with ease.

- 🔗 Download Ollama: https://ollama.com/download  
- Pull the Mistral model:
  ```bash
  ollama pull mistral
2️⃣ Install Python Dependencies
Ensure Python 3.10+ is installed.


pip install -r requirements.txt
3️⃣ Add PDFs & Create Vector DB
Place your PDF files inside the data/company_docs/ folder.


python ingest.py
This script will:

Load PDF files

Split and embed the documents using all-MiniLM-L6-v2

Save the vector index using FAISS to vectordb/

4️⃣ Launch the Streamlit UI
bash
Copy
Edit
streamlit run app.py
You’ll get a web interface to ask questions about the uploaded documents.

💬 Example Questions to Ask
“What is the process for leave approval?”

“Summarize the company policy on remote work.”

“What does the contract say about notice period?”

“Give me bullet points from the vacation policy.”

🛠️ Tech Stack (Free & Local)
Component	Tool / Library
Embedding Model	sentence-transformers (MiniLM)
Vector Database	FAISS (offline, fast)
LLM	Ollama + Mistral (open-source)
UI	Streamlit
RAG Framework	LangChain

🚀 Features
💾 Offline document retrieval

📄 Supports PDF ingestion

🔍 Semantic search

🧠 Local LLM for privacy & speed

🪶 Lightweight and open-source

📌 Notes
Make sure Ollama is running before launching the app.

You can customize the LLM in rag_engine.py (e.g., try llama2, gemma, etc. with ollama pull llama2).

All document embeddings are stored in vectordb/.

