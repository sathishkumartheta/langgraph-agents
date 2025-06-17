from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage

load_dotenv()

model=ChatOpenAI(
    model="gpt-3.5 turbo",
    temperature=0.0
)

def get_model():
    return model
