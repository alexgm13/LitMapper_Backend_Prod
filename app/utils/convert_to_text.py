import fitz  
import re

def clean_text(text: str) -> str:
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_text_from_pdf_stream(file_content: bytes) -> str:
    try:
        doc = fitz.open(stream=file_content, filetype="pdf")
        
        full_text = []
        for page in doc:
            full_text.append(page.get_text())
        
        combined_text = "\n".join(full_text)
        
        final_text = clean_text(combined_text)
        
        return final_text
        
    except Exception as e:
        raise ValueError(f"Error procesando PDF: {str(e)}")