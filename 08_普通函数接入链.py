# lambda ai_msg: {"name": ai_msg.content}匿名函数
# 相当于
# def func(ai_msg):
#     return {"name": ai_msg.content}
# 输入是AIMessage 对象
# 输出是dict 字典
# my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})
# RunnableLambda这个函数是将自定义的一个匿名函数封装成一个可以在chain中链接的对象
#JsonPutputParser转换器，可以将AIMessage类型转为字典格式
from langchain_ollama import*
from langchain_core.prompts import *
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.runnables import RunnableLambda
#创建所需的解析器
strparser=StrOutputParser()
jsonparser=JsonOutputParser()

#初始化模型
model = ChatOllama(model="deepseek-r1")

#初始化提示词模板
#第一个提示词模板
first_prompt = ChatPromptTemplate.from_messages(
        [
            ("system","""你现在是一位{role},请你回答下面这个问题，回答尽量简短一点"""),
            MessagesPlaceholder("chat_history"),
            ("human","{input}")
        ]
)
chat_history_list = [
    ("human", "你好，请问什么是机器学习？"),
    ("ai", '{"last_chat": "机器学习是让计算机从数据中学习规律，而不用显式编程的技术。"}'),
    ("human", "那它和深度学习有什么区别？"),
    ("ai", '{"last_chat": "深度学习是机器学习的一个分支，主要使用多层神经网络来处理复杂特征。"}'),
    ("human", "可以举个生活中的例子吗？"),
    ("ai", '{"last_chat": "比如手机人脸识别、视频推荐，都是深度学习在实际中的应用。"}')
]
#第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "请你从这段对话中提取需要学习的技术栈，{last_chat}"
)
# 使用自定义的函数将AIMessage转换为字典类
my_func = RunnableLambda(lambda ai_meg:{"last_chat":ai_meg.content})
chain = first_prompt | model | my_func  | second_prompt | model | strparser
for chunk in chain.stream({"role":"资深程序员","chat_history":chat_history_list,"input":"如何实现通过摄像头识别手部姿势然后控制前端中的粒子效果呢"}):
    print(chunk,end = "",flush = True)
