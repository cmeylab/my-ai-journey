from __future__ import annotations
from enum import Enum
from dataclasses import dataclass

class Category(Enum):
    INCOME="收入"
    EXPENSE="支出"
@dataclass
class Record:
    category:Category
    amount:float
    note:str=""
