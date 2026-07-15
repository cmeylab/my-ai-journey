from __future__ import annotations
#类型注解,变量
name: str="小明"
age: int=20
scores: list[int]=[85,92,78]
#字典+if
student: dict[str,str|int]={"name":name,"age":age}
if student["age"]>=18:
    print(f"{student['name']}成年了")
#循环
for score in scores:
    if score>=90:
        print(f"优秀:{score}")
#函数(带注解):
def calculate_average(nums:list[int])->float:
    return sum(nums)/len(nums) if nums else 0.0
print(f"平均分:{calculate_average(scores)}")
#函数练习
def greet(name:str,greeting:str="Hello")->str:
    return f"{greeting},{name}! "

