import os
from docx import Document
from pdfminer.high_level import extract_text

def extract_text_from_resume(resume_file):
    """Extracts text from PDF or DOCX resume"""
    file_ext = os.path.splitext(resume_file.name)[1].lower()
    
    if file_ext == ".pdf":
        return extract_text(resume_file)
    
    elif file_ext == ".docx":
        doc = Document(resume_file)
        return "\n".join([para.text for para in doc.paragraphs])
    
    return None
