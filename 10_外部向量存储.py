#可以存储到本地文件
#导包
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
#初始化
vector_store = Chroma(
    collection_name="first_vector_store",#向量库的名称
    embedding_function=DashScopeEmbeddings(),#嵌入模型的名称
    persist_directory=""
)