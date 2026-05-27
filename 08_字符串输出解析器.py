#model可以接入字符串类型,PromptValue类型,消息链表
#模板用invoke或format的方法输出的结果是PromptValue类型
#而model的输出为AIMessage类型，无法继续用|直接连接到下一个model中
#StrOutputtParser是Langchain中内置的字符串解析器，可以将AIMessage解析为简单的字符串类型，的的是Runnable接口的子类
from langchain_classic.chains.summarize.refine_prompts import prompt_template
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import *


#初始化模型
model=ChatOllama(model="deepseek-r1")

#创建聊天模板
prompt_template=PromptTemplate.from_template(
    "我是一个古诗的重度爱好者，我的姓为{name}，请为我的女孩起名,只给出一个名字不要其他的废话"
)
#创建解析器
strOutputParser=StrOutputParser()
chain=prompt_template|model|strOutputParser
res = chain.invoke({"name":"吴"})
print(res)
