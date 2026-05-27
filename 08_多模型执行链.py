#JsonPutputParser转换器，可以将AIMessage类型转为字典格式
from langchain_ollama import*
from langchain_core.prompts import *
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
#创建所需的解析器
strparser=StrOutputParser()
jsonparser=JsonOutputParser()

#初始化模型
model = ChatOllama(model="deepseek-r1")

#初始化提示词模板
#第一个提示词模板
chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system","""你现在是一位{role},请你回答下面这个问题,并且将回答分装为JSON格式，key是last_chat,value就是你的回答，输出格式必须是：
{{"last_chat": "你的回答内容"}}
请严格遵守！"""),
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
prompt_template = PromptTemplate.from_template(
    "请你从这段对话中提取需要学习的技术栈，{last_chat}"
)

#构建链
chain = chat_prompt|model|jsonparser|prompt_template|model|strparser
res = chain.invoke({"role":"学习路线规划大师","chat_history":chat_history_list,"input":"什么是深度学习"})
print(res,type(res))
