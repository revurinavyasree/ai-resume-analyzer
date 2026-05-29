import pdfplumber
from docx import Document


def extract_text(filepath):

    text = ""

    if filepath.endswith(".pdf"):

        with pdfplumber.open(filepath) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    elif filepath.endswith(".docx"):

        doc = Document(filepath)

        for para in doc.paragraphs:

            text += para.text + "\n"

    return text