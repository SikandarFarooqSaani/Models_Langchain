from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
 
documents = [
    "Delhi is capital of India",
    "Peshawar is capital of KPK",
    "Paris is capital of France",
    "Capital of Turkey is Ankara"
]
result = embedding.embed_documents(documents)

print(str(result))