from __future__ import annotations
import json
import logging
from pathlib import Path
from .models import Category,Record

logger=logging.getLogger(__name__)
DATA_FILE = Path("data")/"account.json"

class AccountBook:
    def __init__(self)->None:
        self.records:list[Record] = []
        self._load()
    def add(self,category:Category,amount:float,note:str="")->None:
        self.records.append(Record(category,amount,note))
        logger.info(f"添加记录: %s %.2f %s",category.value,amount,note)
    def balance(self)->float:
        total=0.0
        for r in self.records:
            total += r.amount if r.category == Category.INCOME else -r.amount
        return total
    def summary(self)->dict[str,float]:
        income=sum(r.amount for r in self.records if r.category == Category.INCOME)
        expense=sum(r.amount for r in self.records if r.category == Category.EXPENSE)
        return {"收入":income,"支出":expense,"结余":income-expense}
    def _save(self)->None:
        DATA_FILE.parent.mkdir(exist_ok=True)
        data=[{"category":r.category.name,"amount":r.amount,"mote":r.note} for r in self.records]
        DATA_FILE.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    def _load(self)->None:
        if not DATA_FILE.exists():
            return
        for item in json.loads(DATA_FILE.read_text(encoding="utf-8")):
            self.records.append(Record(Category[item["category"]],item["amount"],item.get("note","")))
    def __del__(self)->None:
        self._save()
