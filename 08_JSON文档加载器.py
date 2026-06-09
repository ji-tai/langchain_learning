from langchain_community.document_loaders import JSONLoader

json_loader = JSONLoader(
    file_path="./data/json/stus_lines.json",
    jq_schema=".name",
    text_content=False,#告知被抽取的结果可以不是字符串
    json_lines=True,#每一行都是json数据
)
json_document = json_loader.load()
print(json_document)