# Import the necessary libraries
import pandas as pd
from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Load the data
df = pd.read_csv("data/transcriptions.csv")
df.head()

# Initialize the OpenAI client
client = OpenAI()



tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_medical_data",
            "description": "Extract patient age, medical specialty, recommended treatment, and ICD-10 code from medical transcription.",
            "parameters": {
                "type": "object",
                "properties": {
                    "age": {
                        "type": "integer",
                        "description": "Age of the patient"
                    },
                    "recommended_treatment": {
                        "type": "string",
                        "description": "Recommended treatment mentioned in the plan section"
                    },
                    "icd_10_code": {
                        "type": "string",
                        "description": "Matching ICD-10 code based on diagnosis"
                    }
                },
                "required": ["age", "medical_specialty", "recommended_treatment", "icd_10_code"]
            }
        }
    }
]


structured_data = []

for _, row in df.iterrows():
    
    prompt = f"""
    Extract the following information from this medical transcription:
    - Patient age
    - Medical specialty
    - Recommended treatment from PLAN section
    - Appropriate ICD-10 code based on diagnosis
    
    Transcription:
    {row['transcription']}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        tools=tools,
        tool_choice={"type": "function", "function": {"name": "extract_medical_data"}}
    )

    tool_call = response.choices[0].message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    # structured_data.append(row['medical_specialty'])
    structured_data.append(arguments)


df_structured = pd.DataFrame(structured_data)

print(df_structured.head())

