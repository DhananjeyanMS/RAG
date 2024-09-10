from dotenv import load_dotenv

import docx
from PyPDF2 import PdfReader

load_dotenv()

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text])
    return text

def read_files(file_paths):
    full_text = ""
    for file_path in file_paths:
        if file_path.endswith('.pdf'):
            full_text += read_pdf(file_path) + "\n"
        elif file_path.endswith('.docx'):
            full_text += read_docx(file_path) + "\n"
    return full_text
