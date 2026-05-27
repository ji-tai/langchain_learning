
from langchain_ollama import *
from langchain_core.prompts import *


# FewShotPromptTemplate(
#     examples=None,示例数据，list，内套字典
#     examples_prompt=None,示例数据的提示词模板
#     prefix=None,组装提示词，示例数据前内容
#     suffix=None,组装提示词，示例数据后内容
#     input_variables=None列表，注入的变量列表
# )
#构建通用提示词模板
prompt_template=PromptTemplate.from_template("单词：{word},反义词：{antonym}")#通用提示词模板
example_data=[
    {"word":"大","antonym":"小"},
    {"word":"上","antonym":"下"}#字典
]
few_shot_prompt = FewShotPromptTemplate(
    examples=example_data,#示例数据模板
    example_prompt=prompt_template,#示例数据  是一个列表可以实现遍历
    prefix="给出给定词的反义词，有如下示例：",#示例的前缀提示词
    suffix="基于示例告诉我：{input_word}的反义词是什么？",#示例的后缀提示词
    input_variables=['input_word']#对suffix注入变量数据
)
model = OllamaLLM(model="deepseek-r1")
prompt_text = few_shot_prompt.invoke(input={"input_word":"左"}).to_string()
for chunk in model.stream(prompt_text):
    print(chunk, end="", flush=True)
