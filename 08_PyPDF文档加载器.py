from langchain_community.document_loaders import PyPDFLoader

pypdf_loader = PyPDFLoader(
    file_path="",
    mode="page",   #读取模式，如果是page则会根据文件的页数获得不同的document,single无论多少页都会获得一个document，默认是page模式
    password="",   #如果文件是加密的，则需要密码参数
)