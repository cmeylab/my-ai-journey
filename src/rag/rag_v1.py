from src.agent.agent_v1 import *
from src.rag.vectordb import *

def build_context(hits:list[dict])->str:
    return "\n\n".join(f"[{h['id']}] {h['text']}" for h in hits)

def rag_answer(question:str,top_k:int=3,db_path:str="./chroma_db")->str:
    collection=get_collection(db_path)
    hits = search_top_k(collection,question,top_k=top_k)
    prompt = (
        "你是一个知识库问答助手。只根据下面的资料回答，不要编造。"
        "如果资料里没有答案，就说'资料中未找到相关信息'。\n\n"
        f"资料:\n{build_context(hits)}\n\n"
        f"问题:{question}"
    )
    return ask_llm([{"role":"user","content":prompt}])