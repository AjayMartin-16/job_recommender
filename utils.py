import docx
import PyPDF2
import re
from io import BytesIO

def parse_resume(file):
    """Extract skills & experience from uploaded resume."""
    text = ""
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        text = file.read().decode("utf-8", errors="ignore")

    skills = re.findall(r"(Python|Java|SQL|Machine Learning|AI|Data Science|JavaScript)", text, re.I)
    exp_match = re.search(r"(\d+)\s+years", text, re.I)
    experience = int(exp_match.group(1)) if exp_match else None

    return {
        "skills": ", ".join(set(skills)) if skills else "",
        "experience": experience
    }
