from __future__ import annotations


def greet(name: str, prefix: str = "你好") -> str:
    return f"{prefix}，{name}"


def sum_all(*nums: int) -> int:
    return sum(nums)


def show_info(**info: str | int) -> None:
    for k, v in info.items():
        print(f"  {k}: {v}")


count: int = 0


def increment() -> None:
    global count
    count += 1


print(greet("小明"))
print(greet("小红", "早上好"))
print(sum_all(1, 2, 3, 4, 5))
show_info(name="小明", age=20, city="北京")
increment()
increment()
print(count)
