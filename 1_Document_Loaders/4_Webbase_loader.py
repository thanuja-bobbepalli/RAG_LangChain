from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt = PromptTemplate(
    template="Ans the folloeing question.\ {question} \n from the following text. \n {text}",
    input_variables=['question','text']
)

url="https://www.flipkart.com/apple-m4-pro-24-gb-512-gb-ssd-macos-sequoia-mx2e3hn-a/p/itmb5a9ed14760c5"

loader=WebBaseLoader(url)
docs =loader.load()

chain = prompt | model | parser
result=chain.invoke({'question':"what is the product description.",'text':docs[0].page_content})


print(result)