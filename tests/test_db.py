from pathlib import Path
import sqlite3
import pytest
from src.db_demo import insert,query_all,query_by_city

@pytest.fixture
def db(tmp_path:Path)->sqlite3.Connection:
    conn = sqlite3.connect(str(tmp_path / "test.db"))
    conn.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER,city TEXT)""")
    conn.commit()
    yield conn
    conn.close()
def test_insert_and_query(db:sqlite3.Connection)->None:
    uid = insert(db,"测试",18,"广州")
    rows=query_all(db)
    assert len(rows)==1
    assert rows[0]==(uid,"测试",18,"广州")
def test_query_by_city(db: sqlite3.Connection) -> None:
    insert(db, "A", 20, "北京")
    insert(db, "B", 25, "上海")
    insert(db, "C", 30, "北京")
    result = query_by_city(db, "北京")
    assert len(result) == 2
