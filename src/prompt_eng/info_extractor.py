from src.prompt_eng.llm_utils import llm_chat
import json
import re

def extract_info(text:str)->dict:
    prompt = f"""从下面这段文字中提取 姓名、电话、地址，只输出 JSON，不要任何其他内容：
    {text}
    要求格式：
    {{"name": "姓名", "phone": "电话", "address": "地址"}}"""
    messages=[{"role":"user","content":prompt}]
    reply=llm_chat(messages,temperature=0)
    return parse_json(reply)
def parse_json(reply:str
               )->dict:
    cleaned = re.sub(r"```json|```", "", reply).strip()
    return json.loads(cleaned)
if __name__=="__main__":
    text = "张三，电话 13812345678，住在北京市海淀区中关村大街1号"
    print(extract_info(text))