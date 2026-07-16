from __future__ import annotations
import json
import logging
from pathlib import Path
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger =logging.getLogger(__name__)
DATA_DIR =Path("data")

def write_todo(text:str)->None:
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / "todo.txt"
    path.write_text(text,encoding="utf-8")
    logger.info("已写入 %s",path)
def read_todo()->str:
    path=DATA_DIR / "todo.txt"
    return path.read_text(encoding="utf-8")
def save_tasks(tasks:list[dict[str,str]])->None:
    DATA_DIR.mkdir(exist_ok=True)
    path=DATA_DIR / "tasks.json"
    path.write_text(json.dumps(tasks,ensure_ascii=False,indent=2),encoding="utf-8")
    logger.info("已保存 %d 条任务", len(tasks))
def load_tasks()->list[dict[str,str]]:
    path=DATA_DIR/"tasks.json"
    if not path.exists():
        logger.warning("文件不存在，返回空列表")
        return []
    return json.loads(path.read_text(encoding="utf-8"))
def divide(a:float,b:float)->float|str:
    try:
        return a/b
    except ZeroDivisionError:
        logger.error("除零错误: %s / %s",a,b)
        return "错误:除数不能为0"
    except TypeError as e:
        logger.error("类型错误: %s",e)
        return f"错误:类型不匹配-{e}"
def main()->None:
    write_todo("学习Day 3:文件与日志")
    print(read_todo())
    tasks=[
        {"name":"写代码","priority":"高"},
        {"name":"跑步","priority":"中"},
    ]
    save_tasks(tasks)
    loaded=load_tasks()
    for t in loaded:
        print(f" {t['name']} ({t['priority']})")
    print(divide(10,2))
    print(divide(10,0))
    print(divide(10,"a"))
if __name__ =="__main__":
    main()