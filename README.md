# DocMind — RAG API

An AI-powered REST API that lets you upload documents and ask questions about them using natural language.

## Tech Stack
- FastAPI
- LangChain
- Groq (LLaMA 3)
- HuggingFace Embeddings
- ChromaDB

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Features
- Upload .txt documents
- Ask questions in natural language
- Beautiful UI at http://127.0.0.1:8000
