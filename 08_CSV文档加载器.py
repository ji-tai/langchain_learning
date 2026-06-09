from langchain_community.document_loaders import CSVLoader

csvloader = CSVLoader(
    file_path="data/csv/student.csv",
    csv_args={
        "delimiter": ",",#指定分隔符
        "quotechar": '"',#指定引用符
        "fieldnames": ["a","b","c"]#指定表头（若原数据没有表头）
    },#csv配置
    encoding="utf-8"
)

# csv_documents = csvloader.load()
# for document in csv_documents:
#     print(document)
for csv_document in csvloader.lazy_load():
    print(csv_document)
#目的是获得document类型的信息