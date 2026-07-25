import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def clean_csv(input_path: str | Path, output_path: str | Path) -> int:
    df = pd.read_csv(input_path, dtype=str, on_bad_lines="skip")
    raw_count = len(df)
    df = df.dropna(how="all").drop_duplicates()
    df.to_csv(output_path, index=False)
    logging.info(f"清洗完成: {raw_count}->{len(df)} 条")
    return len(df)


def main() -> None:
    clean_csv(DATA_DIR / "dirty.csv", DATA_DIR / "clean.csv")


if __name__ == "__main__":
    main()
