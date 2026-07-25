from __future__ import annotations

name: str = "小明"
age: int = 18
score: float = 89.0
tags: list[str] = ["基础", "新手"]
info: dict[str, str | int] = {"city": "北京", "year": 2026}

if age >= 18:
    print(f"{name} 是成年人")
else:
    print(f"{name} 不是成年人")

for t in tags:
    print(f"标签: {t}")


def add(a: int, b: int) -> int:
    return a + b


print(add(3, 5))
