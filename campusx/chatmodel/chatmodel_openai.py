from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatOpenAI(model='gpt-5-mini', 
                   api_key=os.getenv("API_KEY"),
                   base_url=os.getenv("BASE_URL"),
                   temperature=0.2,
                #    top_p=0.8,
                   max_completion_tokens=100
                   )

result = model.invoke("Just Write a 5 lines on Football")

print(result.content)