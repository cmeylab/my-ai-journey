from __future__ import annotations

import json
import logging
from pathlib import Path

DATA_DIR = Path("data")


def writetodo(test: str) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / "todo.txt"
    path.write_text(test, encoding="utf-8")


def readtodo() -> str:
    path = DATA_DIR / "todo.txt"
    return path.read_text(encoding="utf-8")


def jsonstore(test: list[dict[str, str]]) -> None:
    path = DATA_DIR / "todo.json"
    path.write_text(json.dumps(test, ensure_ascii=False, indent=2), encoding="utf-8")


def readjson() -> list[dict[str, str]]:
    path = DATA_DIR / "todo.json"
    if not path.exists():
        return []
    result: list[dict[str, str]] = json.loads(path.read_text(encoding="utf-8"))
    return result


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def divide(a: float, b: float) -> float | str:
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("除零错误: %s / %s", a, b)
        return "错误: 除数不能为 0"
    except TypeError as e:
        logger.error("类型错误: %s", e)
        return f"错误: 类型不匹配 — {e}"


writetodo("test")
print(readtodo())

tasks = [{"score": "89", "name": "xiaoming"}]
jsonstore(tasks)
print(readjson())

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))  # type: ignore[arg-type]
