# import fitz  # PyMuPDF

# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     full_text = ""
#     for page_num in range(doc.page_count):
#         page = doc.load_page(page_num)
#         full_text += page.get_text()
#     return full_text

# extract_text.py
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, chunk_size=1000):
    """
    Extracts text from a PDF and chunks it into smaller parts (chunks of text) to avoid overflow.
    """
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        full_text += page.get_text()
    
    # Split text into smaller chunks
    chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]
    return chunks
