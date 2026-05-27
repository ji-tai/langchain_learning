#链是langchain中的一个串联，将上一个组件的输出作为下一个组件的输入
#可以构建链的前提，各个组件是rannable的组件//特点是rannable组件都是有invoke和stream的接口可以输出
#invoke是一个输入接口，模板需要注入字典，模型需要注入完整字符串
#stream是一个流式输出接口，需要注入字符串
#所以fewshort模板与chat模板的输出不是字符串，但用链结构可以很好的解决这一问题，链内会自主转化，将类型匹配
from langchain_core.prompts import *
from langchain_ollama import *

#定义模型
model = ChatOllama(model="deepseek-r1")

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你现在是一位唐朝的婉约派诗人"),
        MessagesPlaceholder("history"),  # 占位符可以导入外部的历史会话消息
        ("human", "好诗，请再为我写一首闺怨词")
    ]
)
history_data = [
    ("human","请写一首闺怨诗"),
    ("ai","梳洗罢，独倚望江楼。过尽千帆皆不是，斜晖脉脉水悠悠。肠断白苹洲。")
]

chain = chat_prompt_template | model
# ans =chain.invoke({"history":history_data})
# #ans是一个AImessage的对象
# print(ans.content)
for chunk in chain.stream({"history":history_data}):
    print(chunk.content, end="", flush=True)
