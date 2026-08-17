from pathlib import Path
from pypdf import PdfReader
from docx import Document

def load_text(path:str)->str:
    p=Path(path)
    if not p.exists():
        raise FileNotFoundError(f"{path} 不存在")
    suffix = p.suffix.lower()
    if suffix == ".pdf":
        reader = PdfReader(str(p))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)
    if suffix == ".docx":
        doc = Document(str(p))
        return "\n".join(para.text for para in doc.paragraphs)
    return p.read_text(encoding='utf-8')
