from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Student:
    school: str = "一中"

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def intro(self) -> str:
        return f"{self.name}，{self.age}岁，来自{self.school}"


class CollegeStudent(Student):
    def __init__(self, name: str, age: int, major: str) -> None:
        super().__init__(name, age)
        self.major = major

    def intro(self) -> str:
        return f"{self.name}，{self.age}岁，专业是{self.major}"


class OrderStatus(Enum):
    PENDING = "待支付"
    PAID = "已支付"
    SHIPPED = "已发货"
    DONE = "已完成"


@dataclass
class Task:
    title: str
    priority: str = "中"
    done: bool = False

    def mark_done(self) -> None:
        self.done = True


def main() -> None:
    s = Student("小明", 18)
    print(s.intro())

    c = CollegeStudent("小红", 22, "计算机")
    print(c.intro())

    print(OrderStatus.PAID.value)
    print(OrderStatus.PAID.name)

    t = Task("写作业", "高")
    print(t)
    t.mark_done()
    print(t)


if __name__ == "__main__":
    main()
