# agent/skills/resume_autofill.py

from PyPDF2 import PdfReader

def parse_resume_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return {
        "name": "John Doe (placeholder)",
        "summary": text[:500]  # Return just a snippet
    }
