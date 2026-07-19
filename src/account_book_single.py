from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

DATA_FILE = Path("data") / "account.json"


class Category(Enum):
    INCOME = "收入"
    EXPENSE = "支出"


@dataclass
class Record:
    category: Category
    amount: float
    note: str = ""


class AccountBook:
    def __init__(self) -> None:
        self.records: list[Record] = []
        self._load()

    def add(self, category: Category, amount: float, note: str = "") -> None:
        self.records.append(Record(category, amount, note))
        logger.info("添加记录: %s %.2f %s", category.value, amount, note)

    def balance(self) -> float:
        total = 0.0
        for r in self.records:
            total += r.amount if r.category == Category.INCOME else -r.amount
        return total

    def summary(self) -> dict[str, float]:
        income = sum(r.amount for r in self.records if r.category == Category.INCOME)
        expense = sum(r.amount for r in self.records if r.category == Category.EXPENSE)
        return {"收入": income, "支出": expense, "结余": income - expense}

    def _save(self) -> None:
        DATA_FILE.parent.mkdir(exist_ok=True)
        data = [{"category": r.category.name, "amount": r.amount, "note": r.note} for r in self.records]
        DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def _load(self) -> None:
        if not DATA_FILE.exists():
            return
        for item in json.loads(DATA_FILE.read_text(encoding="utf-8")):
            self.records.append(Record(Category[item["category"]], item["amount"], item.get("note", "")))

    def __del__(self) -> None:
        self._save()


def main() -> None:
    book = AccountBook()
    book.add(Category.INCOME, 5000, "工资")
    book.add(Category.EXPENSE, 120, "午饭")
    book.add(Category.EXPENSE, 15.5, "咖啡")
    book.add(Category.INCOME, 200, "红包")
    print(f"余额: {book.balance():.2f}")
    for k, v in book.summary().items():
        print(f"  {k}: {v:.2f}")


if __name__ == "__main__":
    main()
