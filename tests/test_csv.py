from collections.abc import Generator
from pathlib import Path

import pytest

from src.csv_cleaner import clean_csv


@pytest.fixture
def dirty_file(tmp_path: Path) -> Generator[Path, None, None]:
    d = tmp_path / "dirty.csv"
    d.write_text("a,b\n1,2\n,\n1,2\n")
    yield d


def test_clean_csv(dirty_file: Path) -> None:
    out = dirty_file.parent / "clean.csv"
    assert clean_csv(dirty_file, out) == 1


def test_clean_csv_output_content(dirty_file: Path) -> None:
    out = dirty_file.parent / "clean.csv"
    clean_csv(dirty_file, out)
    result = out.read_text()
    assert result == "a,b\n1,2\n"
