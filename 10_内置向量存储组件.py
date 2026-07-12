#依旧只是在内存中存储，程序关闭就会停止
#导包
from langchain_core.vectorstores import InMemoryVectorStore#导入向量存储组件
from langchain_community.embeddings import DashScopeEmbeddings#导入阿里云的官方向量嵌入模型
#初始化向量存储库
Vector_Store = InMemoryVectorStore(embeddings = DashScopeEmbeddings())#直接使用类的默认构造函数
#添加文档到向量库

#删除文档到向量库

#相似性查询

