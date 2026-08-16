import ast
import operator
from datetime import datetime
from pathlib import Path
from src.agent.schemas import validate_args

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
}

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
def get_current_time()->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def _calc(node):
    if isinstance(node,ast.Expression):
        return _calc(node.body)
    if isinstance(node,ast.Constant):
        if isinstance(node.value,(int,float)):
            return node.value
        raise ValueError("只支持数字")
    if isinstance(node,ast.BinOp):
        left = _calc(node.left)
        right = _calc(node.right)
        op = OPS.get(type(node.op))
        if op is None:
            raise ValueError(f"不支持的操作: {type(node.op).__name__}")
        return op(left,right)
    if isinstance(node,ast.UnaryOp):
        oper=OPS.get(type(node.op))
        return oper(0,_calc(node.operand))
    raise ValueError("不支持的表达式")
def calculator(expression:str)->float:
    tree = ast.parse(expression,mode="eval")
    return _calc(tree)
def search_local_docs(keyword:str,max_results:int = 5)->str:
    hits= []
    for f in DATA_DIR.rglob("*"):
        if not f.is_file() or f.suffix in (".pyc",".db",".sqlite"):
            continue
        try:
            text = f.read_text(encoding="utf-8",errors="ignore")
        except OSError:
            continue
        if keyword in f.name or keyword in text:
            hits.append(f"{f.relative_to(DATA_DIR)}")
    if not hits:
        return f"未找到包含 '{keyword}'的文件"
    return "\n".join(hits[:max_results])

FUNCTIONS = {
    "get_current_time":get_current_time,
    "calculator":calculator,
    "search_local_docs":search_local_docs,
}

def call_tool(name:str,arg:dict)->str:
    if name not in FUNCTIONS:
        return f"未知工具: {name}"
    arg = validate_args(name, arg)
    return str(FUNCTIONS[name](**arg))
