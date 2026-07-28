import re
from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def read_log(path: str | Path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z]+", text.lower())


def top_words(text: str, n: int = 10) -> list[tuple[str, int]]:
    return Counter(tokenize(text)).most_common(n)


def main() -> None:
    text = read_log(DATA_DIR / "sample.log")
    for word, count in top_words(text):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
