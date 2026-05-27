from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import *
#支持注入任意数量的历史会话信息
#ps:用from_template仅能接入一条消息，而from_message可以接入一个list的消息
#在之前的通用提示词模板中用的是from_template,

#动态消息的注入
chat_promot=ChatPromptTemplate.from_messages(
    [
        ("system","你现在是一位唐朝的婉约派诗人"),
        MessagesPlaceholder("history"),#占位符可以导入外部的历史会话消息
        ("human","好诗，请再为我写一首闺怨词")
    ]

)
history_data = [
    ("human","请写一首闺怨诗"),
    ("ai","梳洗罢，独倚望江楼。过尽千帆皆不是，斜晖脉脉水悠悠。肠断白苹洲。")
]#这个列表中放的是元组，不是字典，两者的主要区别是，字典是多个键值对，而元组是一个二元组合
chat_text=chat_promot.invoke({"history":history_data})
print(chat_text,type(chat_text))
models=ChatOllama(model="deepseek-r1")
# res=models.invoke(chat_text)
# print(res.content)    res是一个包含了很多东西的类包括消息时间等等
