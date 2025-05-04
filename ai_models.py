import os
from dotenv import load_dotenv
import openai



#-------------------------------------
#Defining chatgpt model to use
#-------------------------------------
# Explicitly specify the .env file path
dotenv_path = "/Users/luisperez/Desktop/AI_Tools/chatgpt.env"

# Load the .env file
load_dotenv(dotenv_path)

# Retrieve the API key correctly (Use the actual variable name)
openai_api_key = os.getenv("OPENAI_API_KEY")  # ✅ Use the correct key name
print(f"API Key Loaded: {openai_api_key is not None}")  # Should print True

# Assign API key to OpenAI
openai.api_key = openai_api_key

# Define model
MODEL_GPT = 'gpt-4o-mini'





#-------------------------------------
#function def for giving suggestions
#-------------------------------------

def get_column_types():
    

column_summary = heart_df.dtypes.reset_index()
column_summary.columns = ['Column Name', 'Data Type']
summary_for_prompt = "\n".join([
    f"{row['Column Name']}: {row['Data Type']}" 
    for _, row in column_summary.iterrows()
])

# Build the prompt
suggestions_prompt = f"""
Given a dataset with the following columns and data types:
{summary_for_prompt}

identify some possible research questions and suggest statistical methods.Please keep them simple enough
that i can assess them quickly and respond using Markdown format. 
"""