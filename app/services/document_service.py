from pathlib import Path
from pypdf import PdfReader


class DocumentService:

    def extract_pdf(self, file_path: str):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return {
            "pages": len(reader.pages),
            "characters": len(text),
            "text": text
        }