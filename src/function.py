from __future__ import annotations
def add_task(name:str,priority:str="中")->dict[str,str]:
    return {"name":name,"priority":priority}
def calculate_sum(*nums:int)->int:
    return sum(nums)
def print_student_info(**info:str|int)->None:
    for k,v in info.items():
        print(f"{k}:{v}")
count:int=0
def increment()->None:
    global count
    count+=1
print(add_task("写作业"))
print(calculate_sum(1,2,3,4,5))
print_student_info(name="小明",age=20)
increment()
print(count)