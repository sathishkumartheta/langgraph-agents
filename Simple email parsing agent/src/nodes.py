from src.message_state import EmailState
from typing import Dict
from pprint import pprint
from src.models import get_model
from src.prompts import spam_detection_prompt, mail_composition_prompt
from src.utils import extract_reason
from langchain_core.messages import SystemMessage,HumanMessage

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

    print('-------- classifying email---------')
    messages=[
        SystemMessage(content=spam_detection_prompt),
        HumanMessage(content=str(state['email']))

    ]
    response=model.invoke(messages)
    response_text=response.content.lower()
    #print(response_text)
    if "legitimate" in response_text:
        is_spam='legitimate'
    else:
        is_spam='spam'

    reason=extract_reason(response_text)
    print(f"This message is classifed as ----:{is_spam}")
    print(f"The reason for classification is ----: {reason}")
    old_messages=state.get("messages")
    new_messages=old_messages+[
        
            {"role": "system", "content": spam_detection_prompt},
            {"role": "user", "content": str(state["email"])},
            {"role": "AI assistant", "content": response_text}
        
    ]
    
    print('-----------------------------------')


    return{
        'is_spam':is_spam,
        'spam_reason':reason,
        'messages':new_messages

    }

   


def delete_email(state:EmailState)->Dict:
    print('\n')
    print('---------------Delete email--------------------')
    print('the email is deleted')
    print('-----------------------------------------------')
    print('\n')
    pass

def compose_email(state:EmailState)->Dict:
    print('\n')
    print('---------------compose email--------------------')
    model=get_model()
    messages=[
        SystemMessage(content=mail_composition_prompt),
        HumanMessage(content=str(state['email']))
    ]
    response=model.invoke(messages)
    #pprint(response.content)
    print('-----------------------------------------------')
    print('\n')
    return {
        'email_draft' : str(response.content)
    }
    pass

def user_approval(state:EmailState)->Dict:
    print('\n')
    print('---------------user approval--------------------')
    print('for your approval')
    print(state['email_draft'])
    print('-----------------------------------------------')
    print('\n')
    pass

def route_email(state:EmailState)->str:
    print('\n')
    print('--------------- inside route email -------------')
    spam=state['is_spam']
    if spam=="spam":
        print('routing to spam')
        print('--------------------------------------------')
        return "spam"
    else:
        print('routing to legitimate')
        print('--------------------------------------------')
        print('\n')
        return "legitimate"
    