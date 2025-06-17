import os
from typing import List,Dict,Any,Optional, TypedDict

from pprint import pprint

from langgraph.graph import START,StateGraph,END

from langchain_openai import ChatOpenAI

from src import message_state
from src import nodes


state=message_state.get_emailstate()

#pprint(state)


builder=StateGraph(state_schema=message_state.EmailState)


builder.add_node("read_email",nodes.read_email)
builder.add_node("classify_email", nodes.classify_email)
builder.add_node("delete_email", nodes.delete_email)
builder.add_node("reply_email", nodes.compose_email)
builder.add_node("user_approval",nodes.user_approval)



builder.add_edge(START,"read_email")
builder.add_edge("read_email", "classify_email")
builder.add_conditional_edges(
    "classify_email",
    nodes.route_email,
    {
        "spam": "delete_email",
        "legitimate":"reply_email"
    }

    
 )
builder.add_edge("delete_email", END)
builder.add_edge("reply_email", "user_approval")
builder.add_edge("user_approval", END)
agent_graph=builder.compile()

#print(graph.get_graph().draw_ascii())

# Example legitimate email
legitimate_email = {
    "sender": "john.smith@example.com",
    "subject": "Question about your services",
    "body": "Dear Mr. Hugg, I was referred to you by a colleague and I'm interested in learning more about your consulting services. Could we schedule a call next week? Best regards, John Smith"
}

# # Example spam email
# spam_email = {
#     "sender": "winner@lottery-intl.com",
#     "subject": "YOU HAVE WON $5,000,000!!!",
#     "body": "CONGRATULATIONS! You have been selected as the winner of our international lottery! To claim your $5,000,000 prize, please send us your bank details and a processing fee of $100."
# }

# Process the legitimate email
print("\nProcessing legitimate email...")
legitimate_result = agent_graph.invoke({
    "email": legitimate_email,
    "is_spam": None,
    "spam_reason": None,
    "email_category": None,
    "email_draft": None,
    "messages": []
})

# # Process the spam email
# print("\nProcessing spam email...")
# spam_result = agent_graph.invoke({
#     "email": spam_email,
#     "is_spam": None,
#     "spam_reason": None,
#     "email_category": None,
#     "email_draft": None,
#     "messages": []
# })
