from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


text_loader = TextLoader(
    file_path="./data/txt文本/mermaid.txt",#文档地址
    encoding="utf-8"#编码格式
)

txt_document = text_loader.load()
print(txt_document)
print(len(txt_document))
#文档分割器返回的数据类型是List[Document]类型
#文本文档加载器只能返回一个Document类型的数据即list大小为1
#为了方便使用langchain官方使用RecursiveCharacterTextSplitter递归字符文档分割器，可以按自然段落分割大型文档

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,#允许的每段最大的字数
    chunk_overlap=100,#两端之间允许重叠的字数
    separators=["\n", "。", "？", "！", ".", "?", "!", " ", ""],#分段依据
    length_function=len   #字符统计的一句，（函数）
)

split_document = splitter.split_documents(txt_document)
print(split_document)
print(len(split_document))

