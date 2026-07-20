from collections import Counter
import re

DATA_DIR="data"
def read_log(path:str)->str:
    with open(path,encoding='utf-8') as f:
        return f.read()
def tokenize(text:str)->list[str]:
    return re.findall(r"[a-zA-Z]+",text.lower())
def top_words(text:str,n:int=10)->list[tuple[str,int]]:
    return Counter(tokenize(text)).most_common(n)
def main()->None:
    text = read_log(f"{DATA_DIR}/sample.log")
    for word,count in top_words(text):
        print(f"{word}: {count}")
if __name__=="__main__":
    main()