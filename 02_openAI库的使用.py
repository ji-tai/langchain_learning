#openAI的使用1.获取客户端的对象，2.调用模型，3.处理结果
#1.获取客户端的对象>>
from openai import OpenAI
client = OpenAI(
api_key="not-needed",#ollama可以不加key
base_url="http://localhost:11434/v1"#一般是有两个参数api_key和base_url由于配置了环境变量所以就不用写api_key

)#创建客户端
#2.创建对话角色/调用模型
message = [
    {"role": "system", "content": "你是一个Python编程专家。"},  # systent是设定角色的性格和设定
    {"role": "assistant", "content": "我是一个Python编程专家。请问有什么可以帮助您的吗？"},  # 实现多轮对话，一般是历史记录
    {"role": "user", "content": "for循环输出1到5的数字"}  # 这个是用户的回答
]#可以将message看作预设历史对话，assistant就是预设AI的回答
response=client.chat.completions.create(
    model="deepseek-r1",
    messages=message#主要包含model和message两个参数
)
#3.处理结果
#AI的回答就在response中
print(response.choices[0].message.content)