from langchain_openai import ChatOpenAI

model=ChatOpenAI(
    model="gpt-3.5 turbo",
    temperature=0.0
)

def get_model():
    return model
