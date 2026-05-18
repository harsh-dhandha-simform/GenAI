from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model = "gpt-5-nano",
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]

res  = model.invoke(messages)

messages.append(AIMessage(content = res.content))
print(messages)