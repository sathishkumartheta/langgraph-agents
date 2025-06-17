from src.message_state import EmailState
from typing import Dict
from pprint import pprint
from src.models import get_model
from src.prompts import spam_detection_prompt

def read_email(state:EmailState) -> Dict :
    print('\n')
    email=state['email']
    print('----- reading email-------')
    print(f"Processing email from '{email['sender']}' on the subject '{email['subject']}'")
    print('-------------------------')
    print('\n')
    return{}

def classify_email(state:EmailState) -> Dict:
    model=get_model()
    messages=[
        SystemMessage(content=spam_detection_prompt)
        HumanMessage(content=state['email'])

    ]
    pass

def delete_email(state:EmailState)->Dict:
    pass

def compose_email(state:EmailState)->Dict:
    pass

def user_approval(state:EmailState)->Dict:
    pass

def route_email(state:EmailState)->str:
    spam=state['is_spam']
    if spam=="spam":
        return "spam"
    else:
        return "legitimate"
    pass