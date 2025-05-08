# # main.py
# from src.rag_system import run_rag_system

# def main():
#     pdf_path = r'D:\Downloads\rag_ai_assistant_complete\data\company_docs\Mustakim_resume-2025.pdf'
    
#     print("AWS RAG System (using free models)")
#     print("Type 'exit' to quit\n")
    
#     while True:
#         query = input("Enter your question: ")
#         if query.lower() == 'exit':
#             break
            
#         answer = run_rag_system(pdf_path, query)
#         print(f"\nAnswer: {answer}\n")

# if __name__ == "__main__":
#     main()
import streamlit as st
from src.rag_system import run_rag_system

# Function to interact with Streamlit UI
def main():
    # Set page title and description
    st.title("Resume RAG System (using free models)")
    st.write("This system allows you to ask questions based on the content of the uploaded PDF document.")
    
    # PDF Path
    pdf_path = r'D:\Downloads\rag_ai_assistant_complete\data\company_docs\Mustakim_resume-2025.pdf'
    
    # Text input for the user's question
    query = st.text_input("Enter your question:", "")

    # Button to trigger the answer generation
    if st.button("Get Answer"):
        if query:
            # Run the RAG system to get the answer
            answer = run_rag_system(pdf_path, query)
            st.write(f"**Answer:** {answer}")
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
