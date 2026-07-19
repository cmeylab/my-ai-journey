from __future__ import annotations
from pathlib import Path
from datetime import datetime
import re

DATA_DIR=Path("data")

def list_files(dir_path:str=".")->list[Path]:
    return [p for p in Path(dir_path).iterdir()if p.is_file()]
def file_info(path:str)->dict[str,str|int]:
    p=Path(path)
    return {
        "name":p.name,
        "size":p.stat().st_size,
        "modified":datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    }
def days_until(target:str)->int:
    target_date=datetime.strptime(target,"%Y-%m-%d")
    return (target_date - datetime.now()).days
def extract_phones(text:str)->list[str]:
    return re.findall(r"1[3-9]\d{9}",text)
def extract_emails(text:str)->list[str]:
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
def main()->None:
    print("文件列表:",[p.name for p in list_files(".")[:5]])
    path = "file_explorer.py"
    print("文件信息:",file_info(path))
    print(f"距离2026-10-01还有 {days_until('2026-10-01')}天")
    sample="联系我: 13800138000 或 admin@example.com,support@test.org"
    print("手机号:",extract_phones(sample))
    print("邮箱:",extract_emails(sample))

if __name__ == "__main__":
    main()