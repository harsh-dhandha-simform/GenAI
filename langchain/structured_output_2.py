from pydantic import BaseModel, Field
from typing import Union
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv  
import os
load_dotenv()

class ContactInfo(BaseModel):
    name: str = Field(description="Person's name")
    email: str = Field(description="Email address")

class EventDetails(BaseModel):
    event_name: str = Field(description="Name of the event")
    date: str = Field(description="Event date")


llm = ChatOpenRouter(
    model = "openai/gpt-oss-20b"
)
agent = create_agent(
    model=llm,
    tools=[],
    response_format=ToolStrategy(Union[ContactInfo, EventDetails])  # Default: handle_errors=True
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th"}]
})
for msg in result["messages"]:
    msg.pretty_print()
 