TOOLS = [
    {
        "name":"get_current_time","description":"获取当前时间",
        "parameters":{"type":"object","properties":{},"required":[]}
    },
    {
        "name": "calculator",
        "description": "数学计算",
        "parameters": {
            "type": "object",
            "properties": {"expression": {"type": "string", "description": "如 3+5*2"}},
            "required": ["expression"]
        }
    },
]
def build_prompt(tools: list[dict]) -> str:
    lines=["你是一个智能助手，你可以使用以下工具:"]
    for t in tools:
        lines.append(f"- {t['name']}: {t['description']}")
    lines.append("当需要工具时，输出格式：")
    lines.append('调用工具: {"name":"工具名", "arg":{...}}')
    lines.append('不需要工具时，直接回答')
    return "\n".join(lines)