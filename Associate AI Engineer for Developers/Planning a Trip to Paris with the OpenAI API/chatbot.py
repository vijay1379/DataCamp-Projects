import os
from openai import OpenAI

# Load API Key from Environment Variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key exists
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set!")

# Define the model to use
model = "gpt-4o-mini"

# Initialize OpenAI Client with API Key
client = OpenAI(api_key=api_key)

conversation = [
    {
        "role":"system",
        "content":'''You are an expert Parisian travel guide representing Peterman Reality Tours. Provide accurate, engaging, and informative answers about Parisian landmarks and culture, ensuring a welcoming and professional tone. If a question is outside your scope, respond with "I am not capable other than tourist guide." '''
    }
]

questions=["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
               "Where is the Arc de Triomphe?",
              "What are the must-see artworks at the Louvre Museum?"]

for q in questions:
    print(f"User:{q}")
    user_dict = {
        "role":"user",
        "content":q 
    }

    conversation.append(user_dict)
    
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        max_tokens=100,
        temperature=0.0
    )

    assistant_dict = {
        "role":"assistant",
        "content":response.choices[0].message.content
    }
    
    conversation.append(assistant_dict)
    print(f"Response : {response.choices[0].message.content}")
    
