from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation"
)

@traceable
def get_model():
    return ChatHuggingFace(llm=llm)

model = get_model()

result = model.invoke("What is the capital of India")

print(result.content)