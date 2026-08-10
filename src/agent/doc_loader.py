from pathlib import Path

def load_text(path:str)->str:
    p=Path(path)
    if not p.exists():
        raise FileNotFoundError(f"{path} 不存在")
    return p.read_text(encoding='utf-8')
