from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1")
res=model.stream(input="你好，为我讲一个小故事吧")
for chunk in res:
    print(chunk,end='',flush=True)