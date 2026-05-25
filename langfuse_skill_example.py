"""
Langfuse Tracing Integration Example for LangChain

This script demonstrates how to use the Langfuse Python SDK to trace LLM and tool calls in a LangChain application, following best practices.
"""
# 1. FIX: Import v3/v4 compatible context propagation and client utilities
from langfuse import observe, get_client, propagate_attributes
from langfuse.langchain import CallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# --- LangChain Setup ---
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

# 2. Automatically capture the wrapper function as the parent trace
@observe()
def traced_invoke(question: str):
    
    # 3. FIX: Use propagate_attributes to contextually pass metadata, 
    # trace name, and user information downstream
    with propagate_attributes(
        trace_name="LangChain QA",
        user_id="example-user",
        metadata={"source": "langchain", "question": question}
    ):
        # 4. Initialize the handler (it binds automatically to the open context)
        langfuse_handler = CallbackHandler()
        
        # 5. Pass the handler into LangChain's configuration array
        result = chain.invoke(
            {"question": question}, 
            config={"callbacks": [langfuse_handler]}
        )
        return result

if __name__ == "__main__":
    answer = traced_invoke("What is Langfuse and how does it work?")
    print("Answer:", answer)
