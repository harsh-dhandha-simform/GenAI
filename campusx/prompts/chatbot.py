from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatOpenAI(
    model = "gpt-5-nano",
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

chat_history = [
    SystemMessage(content = 'You are a helpful AI assistant')
]

while True:
    user_input = input('You:')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content = res.content))
    print("AI:", res.content)

print(chat_history)
    