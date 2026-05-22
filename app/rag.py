from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

vectorstore = None

def process_document(file):
    global vectorstore
    content = file.file.read().decode("utf-8")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents([content])

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(chunks, embeddings)
    return vectorstore

def query_document(question: str):
    if not vectorstore:
        return "No document uploaded yet."

    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
    retriever = vectorstore.as_retriever()
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"
    response = llm.invoke(prompt)
    return response.content