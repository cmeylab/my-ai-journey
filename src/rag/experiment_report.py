import tempfile
from pathlib import Path

from src.agent.doc_loader import load_text
from src.agent.text_splitter import split_text
from src.rag.vectordb import add_chunks, get_collection, search_top_k


def build_kb(files:list[str],chunk_size:int,method:str="sentences")->object:
    collection=get_collection(tempfile.mkdtemp())
    for f in files:
        text = load_text(f)
        chunks= split_text(text,method=method,chunk_size=chunk_size)
        ids = [f"{Path(f).stem}_{i}" for i in range(len(chunks))]
        add_chunks(collection,ids,chunks)
    return collection

def run_experiment(files:list[str],query:str)-> None:
    for chunk_size in (200,500):
        for top_k in (2,3):
            col = build_kb(files,chunk_size)
            hits = search_top_k(col,query,top_k=top_k)
            print(f"\n===chunk_size={chunk_size} top_k={top_k} ===")
            for h in hits:
                print(f" [{h['id']}] dist = {h['distance']:.3f} {h['text'][:50]}")

if __name__ == "__main__":
    docs = [str(p) for p in Path("data").glob("*.pdf")]
    run_experiment(docs,"你的测试问题")