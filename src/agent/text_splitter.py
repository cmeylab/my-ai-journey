import re

def split_by_chars(text:str,chunk_size:int=200,overlap:int=20)->list[str]:
    if chunk_size<=0:
        raise ValueError("chunk_size 必须大于0")
    step = max(1,chunk_size-overlap)
    return [text[i:i+chunk_size] for i in range(0,len(text),step)]
def split_by_sentences(text:str,chunk_size:int=200,overlap:int =20)->list[str]:
    sentences = re.split(r"(?<=[。！？.!?])\s*",text)
    sentences = [s.strip() for s in sentences if s.strip()]
    chunks,buf,buf_len = [],"",0
    for s in sentences:
        if buf_len + len(s) > chunk_size and buf:
            chunks.append(buf)
            buf=s
            buf_len= len(s)
        else:
            buf+=s
            buf_len += len(s)
    if buf:
        chunks.append(buf)
    return chunks
def split_by_paragraphs(text:str,chunk_size:int=200,overlap:int=20)->list[str]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks,buf = [],""
    for para in paras:
        if len(buf) + len(para) >chunk_size and buf:
            chunks.append(buf)
            buf=para
        else:
            buf +=para + "\n"
    if buf:
        chunks.append(buf)
    return chunks
SPLITTERS ={
    "chars":split_by_chars,
    "sentences":split_by_sentences,
    "paragraphs":split_by_paragraphs,
}
def split_text(text:str,method:str="paragraphs",**kwargs)->list[str]:
    return SPLITTERS[method](text,**kwargs)