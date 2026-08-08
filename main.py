from pathlib import Path

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from app.services.document_service import DocumentService
from app.services.vector_service import VectorService

app = FastAPI()

document_service = DocumentService()
verctor_service = VectorService()

UPLOAD_FOLDER = "documents"

Path(UPLOAD_FOLDER).mkdir(exist_ok=True)


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    result = document_service.extract_pdf(file_location)

    chunks = document_service.chunk_text(result["text"])

    stored_chunks = verctor_service.store_chunks(chunks,file.filename)

    return {
        "filename": file.filename,
        "pages": result["pages"],
        "characters": result["characters"],
        "chunks_created": len(chunks),
        "chunks_stored": stored_chunks
    }