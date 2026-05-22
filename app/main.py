from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.rag import process_document, query_document

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def root():
    return FileResponse("app/static/index.html")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    result = process_document(file)
    return {"message": f"{file.filename} uploaded and processed!"}

@app.post("/query")
async def query(question: str):
    answer = query_document(question)
    return {"answer": answer}