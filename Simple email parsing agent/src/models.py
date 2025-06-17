from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import openai

load_dotenv()

model=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.0
)

def get_model():
    return model
