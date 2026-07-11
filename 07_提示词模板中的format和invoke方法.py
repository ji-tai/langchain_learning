#PromptTemplate,FewShotPromptTemplate,ChatProomptTemplate都拥有format和invoke这两类方法
#format，返回字符串类的对象纯字符串替换，解析占位符，生成提示词，返回值是字符串
#invoke，返回promptvalue类对象，支持解析{}占位符和MessagesPlaceholder结构化占位符需要加上一个.to_string()
from langchain_core.prompts import *

"""
继承关系
    PromptTemplate->StringPromptTemplate->StringPromptTemplate->String->BasePromptTemplate
    FewShotPromptTemplate->StringPromptTemplate->StringPromptTemplate->String->BasePromptTemplate
    ChatPromptTemplate->BaseChatPromptTemplate->BasePromptTemplate->BasePromptTemplate
"""

prompt_template=PromptTemplate.from_template("你是一个{role}，请为我{doingsomething}")#简写版
res1=prompt_template.format(role="学业规划师",doingsomething="规划python爬虫的学习路线")#现在返回的是字符串形
res2=prompt_template.invoke({"role":"学业规划师","doingsomething":"规划python爬虫的学习路线"})#invoke需要传入的是一个字典
print(res1,type(res1))
print(res2,type(res2))
# prompt = PromptTemplate(
#     template="你是{角色}，请回答：{问题}",  # 模板内容
#     input_variables=["角色", "问题"],       # 必须写清楚有哪些变量
# )