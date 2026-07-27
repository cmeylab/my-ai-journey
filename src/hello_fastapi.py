from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root()->dict[str,str]:
    return {"message":"Hello FastAPI"}
@app.get("/hello/{name}")
def hello(name:str)->dict[str,str]:
    return {"hello":name}