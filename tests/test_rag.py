import pytest

from src.rag.vectordb import get_collection,add_chunks
from src.rag.rag_v1 import rag_answer

@pytest.fixture
def db_path(tmp_path):
    path = str(tmp_path / "db")
    col = get_collection(path)
    add_chunks(col,["a","b"],["年假有5天。","报销需要发票"])
    return path
def test_rag_answers_about_vacation(db_path):
    answer = rag_answer("年假有几天",top_k=1,db_path=db_path)
    assert "5" in answer
def test_rag_no_hallucination(db_path):
    answer = rag_answer("公式股票代码是什么"，top_k=1,db_path=db_path)
    assert ("未找到" in answer) or ("没有" in answer)

def test_rag_top1_is_relevant_chunk(db_path):
    from src.rag.vectordb import search_top_k
    hits = search_top_k(get_collection(db_path),"年假",top_k=1)
    assert hits[0]["id"] == "a"