import pdfplumber
from docx import Document

def extract_text(file):
    name = file.name.lower()

    if name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += (page.extract_text() or "") + "\n"
        return text.strip()

    elif name.endswith(".doc") or name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    return file.read().decode("utf-8", errors="ignore")
