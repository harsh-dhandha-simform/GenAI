from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI               ## uncomment this if using openai model
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os
load_dotenv()

@tool
def word_count(text: str) -> int:
    """Counts the number of words in the given text."""
    return len(text.split())

tools = [ word_count,DuckDuckGoSearchRun(),]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools when needed."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# llm = ChatOpenAI(
#     model='gpt-3.5-turbo',
#     base_url=os.getenv("BASE_URL"),                ## uncomment this if using openai model
#     api_key=os.getenv("API_KEY"),
#     temperature=0.5,)

llm = ChatOpenRouter(
    model = "openai/gpt-oss-20b"
)
agent = create_tool_calling_agent(llm, tools,prompt)
executor = AgentExecutor(agent=agent, tools=tools,verbose=True)
response = executor.invoke({"input": "Search for LangChain and count the words in the first result"})
print(response["output"])