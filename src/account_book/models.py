from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    INCOME = "收入"
    EXPENSE = "支出"


@dataclass
class Record:
    category: Category
    amount: float
    note: str = ""
