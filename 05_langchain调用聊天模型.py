#聊天模型是针对大语言模型进行的优化，可以支持多轮会话
# AIMessage:相当于assistant
# HumanMessage:相当于user
# SystemMessage:相当于system
#单独使用HumanMwssage
from langchain_community.chat_models.tongyi import ChatTongyi
#从社区版导入同义聊天模型类
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
#导入humanmessage的类
chatmodel = ChatTongyi(model="qwen3-max")
#初始化模型
message = [
    SystemMessage(content="你现在一位中国古代的婉约派词人"),
    HumanMessage(content="请你写一首关于闺怨的词"),
    AIMessage(content="梳洗罢，独倚望江楼。过尽千帆皆不是，斜晖脉脉水悠悠。肠断白苹洲。"),
    HumanMessage(content="请你点评一下这首诗词")
]
#准备消息
for chunk in chatmodel.stream(input=message):
    print(chunk.content,end="",flush=True)
