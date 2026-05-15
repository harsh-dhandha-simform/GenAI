from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
import os
load_dotenv()


# ingest a web page
# loader = WebBaseLoader("https://freedium-mirror.cfd/https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://medium.com/thedeephub/teacher-forcing-in-machine-learning-4a51e12a0c59&ved=2ahUKEwixo-eIzbCUAxU8fvUHHXkUAzwQFnoECCIQAQ&usg=AOvVaw3wWvz4U2mh9xU4Ej3Ez_nX ")
loader = WebBaseLoader("https://medium.com/thedeephub/teacher-forcing-in-machine-learning-4a51e12a0c59")
docs = loader.load()
chunks = RecursiveCharacterTextSplitter(chunk_size=1000).split_documents(docs)
print(chunks[0].page_content) 

vectordb = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
    ),
)
print("\n\n\n" + vectordb.similarity_search("What is teacher forcing?")[0].page_content)
print(vectordb._collection.get(include=['embeddings']))
retriever = vectordb.as_retriever()
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input} {context}"),
])
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant that extracts only URLs from documents."),
#     ("human", "Extract all links from the following whole context. Do not give any other information.\n\nContext:\n{context}\n")
# ])
# build the RAG Chain
doc_chain= create_stuff_documents_chain(llm,prompt)
rag_chain = create_retrieval_chain(retriever, doc_chain)
result = rag_chain.invoke({"input": " Summarize the article in 5 lines in points"})
print(result["answer"])

