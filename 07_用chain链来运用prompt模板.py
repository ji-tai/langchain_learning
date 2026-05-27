from langchain_core.prompts import *
from langchain_ollama import *
prompt_template = PromptTemplate.from_template(
    "你现在是一位古代豪放派的诗人，你的诗词{feacture}，你生活的朝代是{time},请写一首诗"
)
modle = OllamaLLM(model="deepseek-r1")
chain = prompt_template | modle#提示词加模型
res = chain.invoke(input={"feacture":"大气高端上档次","time":"唐朝"})
print(res)