from pathlib import Path
import sqlite3

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DB_PATH=DATA_DIR / "app.db"
def init_db()->sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT NOT NULL,age INTEGER,city TEXT)""")
    conn.commit()
    return conn
def insert(conn:sqlite3.Connection,name:str,age:int,city:str)->int:
    cur = conn.execute("INSERT INTO users (name,age,city) VALUES (?,?,?)",(name,age,city))
    conn.commit()
    return cur.lastrowid
def query_all(conn:sqlite3.Connection)->list[tuple]:
    return conn.execute("SELECT *FROM users").fetchall()
def query_by_city(conn:sqlite3.Connection,city:str)->list[tuple]:
    return conn.execute("SELECT * FROM users WHERE city=?",(city,)).fetchall()
def main() -> None:
    conn = init_db()
    insert(conn, "张三", 20, "北京")
    insert(conn, "李四", 22, "上海")
    insert(conn, "王五", 21, "北京")
    print("全部用户:", query_all(conn))
    print("北京用户:", query_by_city(conn, "北京"))
    conn.close()

if __name__ == "__main__":
    main()