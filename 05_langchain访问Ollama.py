from langchain_ollama import OllamaLLM

llms = OllamaLLM(model="deepseek-r1")
res=llms.invoke(input="你是谁")
print(res)