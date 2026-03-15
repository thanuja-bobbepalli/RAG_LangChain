from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
import time
s=time.time()
loader =DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs =loader.lazy_load()
for doc in docs:
    print(doc.metadata)
e=time.time()

print("time is ",e-s)