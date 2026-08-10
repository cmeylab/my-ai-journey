def split_text(text:str,chunk_size:int=200)->list[str]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks,buf = [],""
    for para in paras:
        if len(buf) + len(para) >chunk_size and buf:
            chunks.append(buf)
            buf=""
        buf +=para + "\n"
    if buf:
        chunks.append(buf)
    return chunks