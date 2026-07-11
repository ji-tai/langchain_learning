from langchain_core.runnables import RunnableLambda
from langchain_ollama import *
from langchain_core.prompts import *
from langchain_core.output_parsers import *
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = OllamaLLM(model = "qwen3.5")
# ptompt = PromptTemplate.from_template(
#     "请根据历史记录回答问题,历史记录是{history},用户提问{input},请回答"
# )
ptompt = ChatPromptTemplate(
    [
        ("system","请根据历史记录回答问题"),
        MessagesPlaceholder("history"),
        ("human","{input}")
    ]
)
str_patsers = StrOutputParser()

#打印提示词的函数
def print_prompt(prompt):
    print("="*10,prompt.to_string(),"="*10)
    return prompt

print_prompt2 = RunnableLambda(print_prompt)#将普通函数改为可以入链的函数

base_chain = ptompt | print_prompt2 | model  | str_patsers

history_store = {}#创建历史会话记录的字典
def get_history(session_id):
    if session_id not in history_store:
        history_store[session_id] = InMemoryChatMessageHistory()
    return history_store[session_id]
#该函数的作用是通过session_id获取对应的历史记录




new_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history"
)

if __name__ == '__main__':
    # 添加配置,添加langchain的配置
    session_config = {
        "configurable":{
            "session_id":"user_001"#配置会话ID，用于查找历史记录
        }
    }
    ans = new_chain.invoke({"input":"小明有两只猫"},session_config)
    print("第一次",ans)
    ans = new_chain.invoke({"input":"小明的妈妈有一只狗，小明的爸爸有三只松鼠"},session_config)
    print("第二次",ans)
    ans = new_chain.invoke({"input":"小明家里总共有几只动物？"},session_config)
    print("第三次",ans)