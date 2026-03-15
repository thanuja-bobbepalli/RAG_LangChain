from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-2.5-flash')
loader=TextLoader(file_path='cricket.txt',encoding='utf-8')
docs=loader.load()
parser=StrOutputParser()

prompt =PromptTemplate(
    template="Give the summary of this topic. \n {topic}",
    input_variables=['topic']

)

chain =prompt | model |parser
result=chain.invoke({'topic':docs[0].page_content})
print(result)