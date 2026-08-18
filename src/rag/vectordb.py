import chromadb
from src.agent.embedder import embed

COLLECTION  = "docs"

def get_collection(path:str="./chroma_db"):
    client = chromadb.PersistentClient(path=path)
    return client.get_or_create_collection(
        name=COLLECTION,
        metadata={"hnsw:space":"cosine"},
    )
def add_chunks(collection,chunk_ids:list[str],texts:list[str])->None:
    collection.add(
        ids=chunk_ids,
        documents=texts,
        embeddings=[embed(t) for t in texts],
    )

def search(collection,query:str,top_k:int=3):
    return collection.query(
        query_embeddings=[embed(query)],
        n_results=top_k,
    )