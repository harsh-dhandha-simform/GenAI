from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}"),
])
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("API_KEY"),           
    base_url=os.getenv("BASE_URL")
)
chain = prompt | llm | StrOutputParser()
print(chain.invoke({"question": "Who are You? which moddel are you using? EXplain in detail your architecture and how you work?"}))