from pathlib import Path

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Body

from app.services.document_service import DocumentService
from app.services.vector_service import VectorService
from app.services.llm_service import LLMService
app = FastAPI()

document_service = DocumentService()
vector_service = VectorService()
llm_service = LLMService()

UPLOAD_FOLDER = "documents"

Path(UPLOAD_FOLDER).mkdir(exist_ok=True)


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    result = document_service.extract_pdf(file_location)

    chunks = document_service.chunk_text(result["text"])

    stored_chunks = vector_service.store_chunks(chunks,file.filename)

    return {
        "filename": file.filename,
        "pages": result["pages"],
        "characters": result["characters"],
        "chunks_created": len(chunks),
        "chunks_stored": stored_chunks
    }

@app.post("/search")
def search_documents(question: str = Body(embed=True)):

    results = vector_service.search(question)

    return results

@app.post("/ask")
def ask_question(
    question: str = Body(embed=True)
):
    results = vector_service.search(
        question,
        top_k=3
    )

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    answer = llm_service.generate_answer(
        question=question,
        context=context
    )

    return {
        "question": question,
        "answer": answer,
        "sources": results["metadatas"][0]
    }