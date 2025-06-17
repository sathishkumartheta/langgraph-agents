from src.message_state import EmailState
from typing import Dict
from pprint import pprint

def read_email(state:EmailState) -> Dict :
    print('\n')
    email=state['email']
    print('----- reading email-------')
    print(f"Processing email from '{email['sender']}' on the subject '{email['subject']}'")
    print('-------------------------')
    print('\n')
    return{}

def classify_email(state:EmailState) -> Dict:
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