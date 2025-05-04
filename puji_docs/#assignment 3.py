#Import Packages
import os
import io
import contextlib
import re
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats
import sklearn as sk

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

#Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
print("KEY LOADED:", openai_api_key)


#Title
st.title("Python Code Assistant")

#Upload Python script
uploaded_file = st.file_uploader("Upload your Python script", type="py")
question = st.text_input("How do you need help with your Python code?")

#Initialize OpenAI LLM
template = """
You are an expert Python developer helping a user improve their code. 
A user has uploaded the following Python sample:

{code_content}

The user asked: "{question}"

Please provide suggestions for improving code quality, readability, and efficiency. Please determine 
any bugs and provide a revised version of the code with comments.
"""
prompt = PromptTemplate(input_variables=["code_content", "question"], template=template)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_chain = prompt | llm

#Main logic
if uploaded_file:
    code_bytes = uploaded_file.read()
    code_content = code_bytes.decode("utf-8")

    st.subheader("Code Preview")
    st.code(code_content, language="python")
    st.write(f"Your script has {len(code_content.splitlines())} lines of code.")

    if st.checkbox("Show raw code text"):
        st.text(code_content)

    if question and st.button("Suggest Improvements"):
        with st.spinner("Analyzing your code..."):
            result = llm_chain.invoke({
                "code_content": code_content,
                "question": question
            })

        st.markdown("Suggestions & Improvements")
        output_text = result.content if hasattr(result, "content") else result
        st.markdown(output_text if output_text else "*No response received from LLM*")
        st.session_state.generated_code = output_text

#Code Execution
if "generated_code" in st.session_state:
    if st.button("Run Revised Code"):
        result = st.session_state.generated_code

        #Extract Python code block from the result
        code_match = re.search(r"```python(.*?)```", result, re.DOTALL)
        if not code_match:
            code_match = re.search(r"```(.*?)```", result, re.DOTALL)

        
        code_to_run = code_match.group(1).strip() if code_match else result
        st.session_state.cleaned_code = code_to_run

        # Show revised code before running
        st.markdown("Revised Code to be Executed:")
        st.code(code_to_run, language="python")

        #Execute code
        #So the tool cannot run turtle code (which was the file I uploaded), need to figure out if/how the tool can run a regular Python script
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                exec(code_to_run, {})
                output = f.getvalue()
                st.success("Code ran successfully!")
                st.text(output)
            except Exception as e:
                st.error(f"Error running code: {e}")

