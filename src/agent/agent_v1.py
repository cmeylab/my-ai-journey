import json
import os

from openai import OpenAI

from src.agent.schemas import build_prompt, TOOLS
from src.agent.tool import call_tool

client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.getenv("API_KEY"),
)
SYSTEM = build_prompt(TOOLS)
MAX_TURN = 5


def ask_llm(messages: list) -> str:
    resp = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        temperature=0,
    )
    return resp.choices[0].message.content


def parse_tool_call(text: str) -> dict | None:
    for line in text.splitlines():
        if line.startswith("调用工具"):
            data = line.split(":", 1)[1].strip()
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return {"name": "__retry__", "arg": {"error": data}}
    return None


def agent_run(question: str) -> str:
    messages = [{"role": "system", "content": SYSTEM}]
    messages.append({"role": "user", "content": question})
    for _ in range(MAX_TURN):
        text = ask_llm(messages)
        messages.append({"role": "assistant", "content": text})

        call = parse_tool_call(text)
        if call is None:
            return text

        if call["name"] == "__retry__":
            messages.append({
                "role": "user",
                "content": "你的输出格式不合法，请严格按 调用工具: {\"name\": ..., \"arg\": {...}} 重新输出"
            })
            continue

        name = call["name"]
        arg = call.get("arg") or call.get("arguments")
        try:
            result = call_tool(name, arg)
        except Exception as e:
            result = f"工具执行出错: {e}"
        print(f"[调用] {name}{arg} -> {result}")
        messages.append({"role": "user", "content": f"工具结果: {result}"})

    return "达到最大轮数，未得出结果"


if __name__ == "__main__":
    print(agent_run("现在是什么时间"))