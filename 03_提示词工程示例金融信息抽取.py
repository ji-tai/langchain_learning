import json
from openai import OpenAI

#创立客户端
client = OpenAI(
    base_url="http://localhost:11434/v1"
)

#创建数据
schema = ["日期", "股票名称", "开盘价", "收盘价", "成交量"]

examples_data = [
    # 示例数据
    {
        "content": "2023-01-10，股市震荡。股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。",
        "answers": {
            "日期": "2023-01-10",
            "股票名称": "强大科技A股",
            "开盘价": "100人民币",
            "收盘价": "102人民币",
            "成交量": "520000"
        }
    },
    {
        "content": "2024-05-16，股市利好。股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。",
        "answers": {
            "日期": "2024-05-16",
            "股票名称": "英伟达美股",
            "开盘价": "105美元",
            "收盘价": "116美元",
            "成交量": "3560000"
        }
    }
]

questions = [
    # 提问问题
    "2025-06-16，股市利好。股票传智教育A股今日开盘价66人民币，一度飙升至70人民币，随后回落至65人民币，最终以68人民币收盘，成交量达到123000。",
    "2025-06-06，股市利好。股票黑马程序员A股今日开盘价200人民币，一度飙升至211人民币，随后回落至201人民币，最终以206人民币收盘。"
]

#设置messages
messages = [
    {'role':'system','content':'你现在是一名资深的金融分析师，你的任务是将一则金融文本中的信息按照["日期", "股票名称", "开盘价", "收盘价", "成交量"]的JSON格式提取出来，如果没有相匹配的信息那么就回答"未得到有用的信息"'}
]

#导入示例代码
for example in examples_data:
    for key, value in example.items():
        if(key == 'content'):
            messages.append({'role':'user','content':value})
        else:
            messages.append({'role':'assistant','content':json.dumps(value,ensure_ascii=False)})#因为需要字符串来传入context需要类型转化
# for example in examples_data:
#     messages.append({'role':'user','content':example['content']})
#     messages.append({'role':'assistant','content':json.dumps(example['answers'],ensure_ascii=False)})

#创建回答
for question in questions:
    response = client.chat.completions.create(
        model='deepseek-r1',
        messages=messages+[{'role':'user','content':f"按照上述的示例，抽取这个句子的信息{question}"}]#我这个字符串里有变量 {question}，请帮我把变量的值填进去！
    )
    print(response.choices[0].message.content)