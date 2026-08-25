import json
import sqlite3

DB_PATH = "knowledge.db"

def build_db()->None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS chunks (id INTEGER PRIMARY KEY,text TEXT,vec TEXT)")
    conn.commit()
    conn.close()

def store(text:str,vec:list[float])->None:
    conn = sqlite3.connect(DB_PATH)
    vec_json=json.dumps(vec)
    conn.execute("INSERT INTO chunks (text,vec) VALUES (?,?)",(text,vec_json))
    conn.commit()
    conn.close()
def search(vec:list[float],top_k:int=3)->list[str]:
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT text,vec FROM chunks").fetchall()
    conn.close()
    ranked=[]
    for text,vec_str in rows:
        other = json.loads(vec_str)
        score = sum(a*b for a,b in zip(vec,other))
        ranked.append((score,text))
    ranked.sort(reverse=True)
    return [t for _,t in ranked[:top_k]]