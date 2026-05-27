from langchain_community.llms.tongyi import Tongyi


#调用通义千问LLM
llms = Tongyi(model="qwen-max")#没有APIkey环境变量的话就需要传入APIkey的参数
#不用qwen3-max,是因为3是聊天模型，而qwen-max是LLMs

#调用invoke向模型提问
res = llms.invoke(input="你是谁")
print(res)