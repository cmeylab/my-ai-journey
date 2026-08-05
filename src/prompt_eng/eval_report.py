import json
from src.prompt_eng.info_extractor import extract_info

TEST_CASES = [
    {"text": "张三，电话 13812345678，住在北京市海淀区中关村大街1号",
     "expected": {"name": "张三", "phone": "13812345678", "address": "北京市海淀区中关村大街1号"}},
    {"text": "李四 13987654321 上海市浦东新区世纪大道100号",
     "expected": {"name": "李四", "phone": "13987654321", "address": "上海市浦东新区世纪大道100号"}},
    {"text": "你好我叫王五，手机13711112222，广州天河区体育西路8号",
     "expected": {"name": "王五", "phone": "13711112222", "address": "广州天河区体育西路8号"}},
    {"text": "赵六电话136-3333-4444 深圳市南山区科技园南路55号",
     "expected": {"name": "赵六", "phone": "136-3333-4444", "address": "深圳市南山区科技园南路55号"}},
    {"text": "我是John Smith，联系电话+86-135-1234-5678，地址是上海市静安区南京西路20弄",
     "expected": {"name": "John Smith", "phone": "+86-135-1234-5678", "address": "上海市静安区南京西路20弄"}},
    {"text": "钱七，13599887766，家在西安市雁塔区高新路",
     "expected": {"name": "钱七", "phone": "13599887766", "address": "西安市雁塔区高新路"}},
    {"text": "孙八的电话是15900001111，住在武汉市武昌区东湖路",
     "expected": {"name": "孙八", "phone": "15900001111", "address": "武汉市武昌区东湖路"}},
    {"text": "周九 15277778888 成都市武侯区人民南路四段",
     "expected": {"name": "周九", "phone": "15277778888", "address": "成都市武侯区人民南路四段"}},
    {"text": "吴十（电话：18866667777）浙江省杭州市西湖区文三路90号",
     "expected": {"name": "吴十", "phone": "18866667777", "address": "浙江省杭州市西湖区文三路90号"}},
    {"text": "郑十一 13799998888 江苏省南京市鼓楼区中山北路",
     "expected": {"name": "郑十一", "phone": "13799998888", "address": "江苏省南京市鼓楼区中山北路"}},
]

def run_eval()->dict:
    correct=0
    for case in TEST_CASES:
        try:
            result = extract_info(case["text"])
        except json.JSONDecodeError:
            result = {"error":"解析失败"}
        is_correct = result ==case["expected"]
        if is_correct:
            correct +=1
        print(case["text"],"->",result,"✓" if is_correct else "✗")
    return {"total":len(TEST_CASES),"correct":correct,"accuracy":correct / len(TEST_CASES)}
if __name__ == '__main__':
    print(run_eval())