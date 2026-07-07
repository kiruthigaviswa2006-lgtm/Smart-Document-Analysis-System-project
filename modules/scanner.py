import os
import json
import filetype

# Load settings
with open("config/settings.json", "r") as file:
    settings = json.load(file)

SUPPORTED_FORMATS = settings["supported_formats"]
INPUT_FOLDER = settings["input_folder"]


def scan_documents():
    documents = []

    for root, dirs, files in os.walk(INPUT_FOLDER):
        for file in files:

            filepath = os.path.join(root, file)

            extension = os.path.splitext(file)[1].lower()

            size = os.path.getsize(filepath)

            kind = filetype.guess(filepath)

            mime = kind.mime if kind else "Unknown"

            if extension in SUPPORTED_FORMATS:
                status = "Supported"
            else:
                status = "Unsupported"

            documents.append({
                "File Name": file,
                "File Path": filepath,
                "Extension": extension,
                "MIME Type": mime,
                "Size (Bytes)": size,
                "Status": status
            })

    return documents