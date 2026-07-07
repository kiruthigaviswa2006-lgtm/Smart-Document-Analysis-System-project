import pdfplumber
import pandas as pd
from docx import Document
import os


def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    try:

        if extension == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        elif extension == ".docx":
            doc = Document(file_path)
            text = "\n".join([p.text for p in doc.paragraphs])
            return text

        elif extension == ".pdf":
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text

        elif extension in [".xlsx", ".csv"]:

            if extension == ".xlsx":
                df = pd.read_excel(file_path)
            else:
                df = pd.read_csv(file_path)

            return df.to_string()

        else:
            return "Unsupported Format"

    except Exception as e:
        return str(e)