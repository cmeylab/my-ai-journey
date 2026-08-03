from src.prompt_eng.llm_utils import llm_chat
SENTENCE = "这个电影太棒了，我看了三遍"
zero_shot_prompt = f"把这句话的情感分类为 积极/消极，只回答一个词：{SENTENCE}"

few_shot_prompt = """请根据下面的例子，把最后一句话分类为 积极/消极，只回答一个词：
天气真好 → 积极
太吵了，睡不着 → 消极
午餐很难吃 → 消极
{0} →""".format(SENTENCE)

cot_prompt = f"""请逐步分析这句话的情感，最后输出 积极/消极：
句子：{SENTENCE}
步骤：
1. 找出表达情感的关键词
2. 判断关键词的情感倾向
3. 得出结论"""

if __name__ =="__main__":
    messages=[{"role":"user","content":zero_shot_prompt}]
    print("===Zero-shot===")
    print(llm_chat(messages))

    messages = [{"role": "user", "content": few_shot_prompt}]
    print("=== Few-shot ===")
    print(llm_chat(messages))

    messages = [{"role": "user", "content": cot_prompt}]
    print("=== CoT ===")
    print(llm_chat(messages))