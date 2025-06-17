from typing import TypedDict,List,Optional, Any, Dict
from pprint import pprint

class EmailState(TypedDict):

    #The email message to read
    email : Dict[str,Any]

    # is_spam=spam indicates spam is_spam=not_spam indicates no spam
    is_spam: Optional[str]

    #category of email: inquiry, thank you etc
    email_category :Optional[str]

    #the reason for the spam
    spam_reason:Optional[str]

    #Response email draft
    email_draft:Optional[str]

    #Metadata storing the conversation with llms
    messages:List[Dict[str,Any]]


def get_emailstate():
    state=EmailState()
    
    return state
