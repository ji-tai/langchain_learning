import json, os
from typing import Sequence

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import messages_from_dict, message_to_dict, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnableWithMessageHistory
from langchain_ollama import OllamaLLM
#BaseChatMessageHistory是一个消息历史的基类
#InMemoryChatMessageHistory直接继承了这个类
#我们的目的是直接重新构建一个新类叫做FillChatMessageHistory
#BaseChatMessageHistory有三个抽象函数
# @property
# def messages(self) -> Sequence[BaseMessage]:
#     """只读属性：返回全部历史消息列表，不能直接append修改"""
#
# def add_messages(self, messages: Sequence[BaseMessage]) -> None:
#     """批量追加多条消息（入参：消息序列list/tuple）"""
#
# def clear(self) -> None:
#     """清空当前会话所有历史"""
class FillChatMessageHistory(BaseChatMessageHistory):#InMemoryChatMessageHistory这个类的基类也是BaseChatMessageHistory
    def __init__(self, session_id: str,storage_path: str):
        self.session_id = session_id    #获取会话ID
        self.storage_pah = storage_path  #存储历史记录的文件夹地址
        self.file_path = os.path.join(storage_path, session_id)
        #如果文件夹路径不就会存在创建一个新的文件夹路径
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)
        new_messages = [message_to_dict(message) for message in all_messages]#将消息转为字典格式
        with open(self.file_path, "w", encoding="utf-8") as f:#若没有文件则会自动创建一个文件名字为self.file_path
            json.dump(new_messages, f)
    @property#该装饰器可以将成员方法变为属性
    def messages(self) -> Sequence[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages = json.load(f)#将字典格式的数据解析为json格式
                return messages_from_dict(messages)
        except FileNotFoundError:
            return []
    def clear(self)-> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


#尝试使用长期对话记忆
model = OllamaLLM(model="qwen3.5")
ptompt = ChatPromptTemplate.from_messages(
    [
        ("system","请根据历史记录回答"),
        MessagesPlaceholder("history"),#消息占位类
        ("human","{input}")
    ]
)

str_patsers = StrOutputParser()

def print_prompt(prompt):
    print("="*30,"\n",prompt.to_string(),"\n","="*30)
    return prompt
#打印提示词
print_prompt2 = RunnableLambda(print_prompt)#将普通函数改为可以入链的函数

chain = ptompt | print_prompt2 | model | str_patsers

def get_history(session_id):
    return FillChatMessageHistory(session_id,"./chat_memory")
new_chain = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history"
)
if __name__ == '__main__':
    session_config = {
        "configurable":{
            "session_id" : "jitai_001"
        }
    }
    # ans = new_chain.invoke({"input":"小明有两只猫"},session_config)
    # print("第一次",ans)
    # ans = new_chain.invoke({"input":"小明的妈妈有一只狗，小明的爸爸有三只松鼠"},session_config)
    # print("第二次",ans)
    ans = new_chain.invoke({"input":"小明家里总共有几只动物？"},session_config)
    print("第三次",ans)

