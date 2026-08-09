# AEC Knowledge Assistant

A local Retrieval-Augmented Generation (RAG) application built with Python and FastAPI that allows users to upload PDF documents and ask questions based on their content.

The application extracts text from uploaded PDFs, creates semantic embeddings using Sentence Transformers, stores them in ChromaDB, retrieves the most relevant document chunks, and generates answers using a locally hosted Llama 3.2 model through Ollama.

---

## Features

- Upload PDF documents
- Extract text using PyPDF
- Split documents into overlapping chunks
- Generate semantic embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Perform semantic similarity search
- Generate grounded answers using Ollama (Llama 3.2)
- Return source metadata with responses
- Interactive API documentation using FastAPI Swagger UI

---

## How it works

The application follows a standard Retrieval-Augmented Generation (RAG) workflow:

1. A PDF document is uploaded.
2. Text is extracted and split into smaller overlapping chunks.
3. Each chunk is converted into an embedding using Sentence Transformers and stored in ChromaDB.
4. When a user asks a question, the question is converted into an embedding.
5. ChromaDB retrieves the most relevant document chunks.
6. The retrieved context and the user's question are sent to a local Llama 3.2 model running through Ollama.
7. The model generates a response based only on the retrieved context.

## Technologies

- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- Ollama (Llama 3.2)
- PyPDF

---

## Available APIs

- Upload – Uploads a PDF, extracts its text, creates embeddings, and stores them in ChromaDB.
- Search – Retrieves the most relevant document chunks using semantic search.
- Ask – Generates an answer using the retrieved document content and the local Llama 3.2 model.

---

## Running the Application

Install the required packages:

```bash
pip install -r requirements.txt
```

Start Ollama (if it is not already running) and download the model:

```bash
ollama pull llama3.2:3b
```

Run the application:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Future Improvements

- Token-aware chunking
- OCR support for scanned PDFs
- Page-level citations
- Metadata filtering
- React frontend
- Docker support
- Azure OpenAI integration
