from src.agent.agent_v1 import agent_run

QUESTIONS = [
    "现在几点",
    "123*456 等于多少",
    "帮我找一下 data 目录里和account 有关的文件",
    "你是谁",
]
for q in QUESTIONS:
    print(f"\nQ:{q}")
    print(f"A:{agent_run(q)}")