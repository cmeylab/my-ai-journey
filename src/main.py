from fastapi import FastAPI

from src.rag.rag_v1 import rag_answer

app = FastAPI()

@app.get("/qa")
def qa(question: str):
    return {"answer": rag_answer(question)}