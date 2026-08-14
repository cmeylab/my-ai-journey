import ast
import operator
from datetime import datetime

from src.agent.schemas import validate_args

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
}

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
FUNCTIONS = {
    "get_current_time":get_current_time,
    "calculator":calculator,
}

def call_tool(name:str,arg:dict)->str:
    if name not in FUNCTIONS:
        return f"未知工具: {name}"
    arg = validate_args(name, arg)
    return str(FUNCTIONS[name](**arg))