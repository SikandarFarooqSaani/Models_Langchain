from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Updated the model name here
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7
)

result = llm.invoke("What is the capital of Pakistan")

# Note: result is an AIMessage object. 
# If you just want the text response, use result.content
print(result.content)