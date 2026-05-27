from langchain_classic.chains.summarize.refine_prompts import prompt_template
from langchain_core.prompts import *
from  langchain_ollama import*

prompt_template = PromptTemplate.from_template(
    "我是一个超级英雄，我的名字是{name}，刚才在{place}，请猜一猜我在干什么"
)
prompt_text = prompt_template.format(name="蜘蛛侠",place="纽约")
#用format方法注入信息
LLM=OllamaLLM(model="deepseek-r1")
for chunk in LLM.stream(input=prompt_text):
    print(chunk,end="",flush=True)
