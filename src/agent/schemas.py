from typing import TypedDict
class ToolParam(TypedDict):
    type:str
    description:str
class ToolSchema(TypedDict):
    name:str
    description:str
    parameters:dict
TOOLS : list[ToolSchema] = [
    {
        "name":"get_current_time",
        "description":"获取当前时间",
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
    {
        "name":"search_local_docs",
        "description":"在本地数据目录按关键词搜索文件内容",
        "parameters":{
            "type":"object",
            "properties":{"keyword":{"type":"string","description":"要搜索的关键词"}},
            "required":["keyword"]
        }
    },
]
def validate_args(name:str,arg:dict)->dict:
    for tool in TOOLS:
        if tool["name"]!=name:
            continue
        required = tool["parameters"].get("required", [])
        missing = [p for p in required if p not in arg]
        if missing:
            raise ValueError(f"缺少必填参数: {missing}")
        return {k:v for k,v in arg.items() if k in tool["parameters"]["properties"]}
    return arg
def build_prompt(tools: list[dict]) -> str:
    lines=["你是一个智能助手，你可以使用以下工具:"]
    for t in tools:
        lines.append(f"- {t['name']}: {t['description']}")
    lines.append("当需要工具时，输出格式：")
    lines.append('调用工具: {"name":"工具名", "arg":{...}}')
    lines.append('不需要工具时，直接回答')
    return "\n".join(lines)