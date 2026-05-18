from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatOpenAI(
    model = "gpt-5-nano",
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

template2 =  PromptTemplate(
    
    template = 'Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

prompt = template2.invoke({'name': 'harsh'})

res = model.invoke(prompt)
print(res.content) 