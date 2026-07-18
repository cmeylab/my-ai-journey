from __future__ import annotations
from pathlib import Path
import pytest
from src.account_book import AccountBook, Category

@pytest.fixture
def book()->AccountBook:
    Path("data/account.json").unlink(missing_ok=True)
    return AccountBook()
def test_add_income(book: AccountBook) -> None:
    book.add(Category.INCOME,1000)
    assert book.balance()==1000
def test_add_expense(book: AccountBook) -> None:
    book.add(Category.INCOME,2000)
    book.add(Category.EXPENSE,500)
    assert book.balance()==1500
def test_summary(book: AccountBook) -> None:
    book.add(Category.INCOME,3000)
    book.add(Category.EXPENSE,300)
    s=book.summary()
    assert s["收入"]==3000
    assert s["支出"]==300
    assert s["结余"]==2700
