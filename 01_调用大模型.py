import os
from openai import OpenAI

# 注意：删除了错误的 messages 导入
# from pyexpat.errors import messages  ← 这行是错的，必须删掉

# 初始化客户端
client = OpenAI(
    # 阿里云通义千问兼容接口，如果要用本地的大模型就需要将该接口改为http://localhost:11434/v1,/v1是OpenAI 兼容 API 路径前缀
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

    # 必须传入 API Key（环境变量或直接写）
    api_key=os.getenv("OPENAI_API_KEY")  # 推荐从环境变量读取
)

# 发起流式请求
completion = client.chat.completions.create(
    model="qwen3.5-plus",  # 修复：这里少了逗号
    messages=[
        {"role": "system", "content": "you are a helpful assistant"},
        {"role": "user", "content": "你好，千问"},
    ],
    stream=True  # 修复：ture → True
)

# 流式输出结果
print("AI 回复：")
for chunk in completion:
    # 提取并打印内容
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)