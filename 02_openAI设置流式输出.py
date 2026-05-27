from openai import OpenAI
client = OpenAI(
api_key="not-needed",
base_url="http://localhost:11434/v1"
)
message = [
    {"role": "system", "content": "你是一个Python编程专家。"},
    {"role": "assistant", "content": "我是一个Python编程专家。请问有什么可以帮助您的吗？"},
    {"role": "user", "content": "for循环输出1到5的数字"}
]
response=client.chat.completions.create(
    model="deepseek-r1",
    messages=message,
    stream=True#开启流式输入
)
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,#默认每一小段以“\n”结束，可以用end=""设置
        end="",
        flush=True#设置print的显示模式，直接显示在屏幕上，不额外存在缓冲区中
    )
#正常
# response
# ├─ id：对话ID
# ├─ object：固定为 chat.completion
# ├─ created：时间戳
# ├─ model：模型名称
# ├─ system_fingerprint：系统标识
# ├─ choices[]  列表
# │  └─ [0]
# │     ├─ index：0
# │     ├─ message
# │     │   ├─ role：assistant
# │     │   ├─ content：回答内容
# │     │   └─ refusal：null（拒绝时才有）
# │     ├─ logprobs：null
# │     └─ finish_reason：stop / length
# └─ usage
#    ├─ prompt_tokens
#    ├─ completion_tokens
#    ├─ total_tokens
#    ├─ prompt_tokens_details
#    └─ completion_tokens_details
#流式
# chunk（每一段）
# ├─ id
# ├─ object：chat.completion.chunk
# ├─ created
# ├─ model
# ├─ system_fingerprint
# └─ choices[]
#    └─ [0]
#       ├─ index：0
#       ├─ delta
#       │   ├─ role：仅第一段
#       │   └─ content：当前片段文字
#       ├─ logprobs：null
#       └─ finish_reason：null / stop