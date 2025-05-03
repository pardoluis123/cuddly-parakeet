#Import Packages
import os
from dotenv import load_dotenv
import streamlit as st
from utilities import load_home_button

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

#Load environment variables from .env file
load_dotenv('/Users/luisperez/Desktop/AI_Tools/envfile.env')
openai_api_key = os.getenv("OPENAI_API_KEY")
print("KEY LOADED:", openai_api_key)

def run_code_improver(current_state):
    ''' Seperating out the module for running our actual code in here

    Parameters
    ----------
    current_state=st.session_state,default=st.session_state
        The session state we recieve from whatever is handling the overarching file. Honestly Streamlit makes this
        an incredibly approachable way to scale the app because we can organize quite nicely into seperate modules
        in various different areas.

    Returns
    ------
        None


    Notes
    -----


    Examples
    --------
    
        
    '''

    #import our current state, intitiate file uploader, and title etc
    current_state=current_state if current_state is not None else st.session_state
    st.title("Python Code Assistant")
    uploaded_file = st.file_uploader("Upload your Python script", type="py")
    
    if uploaded_file:
        llm_chain=initialize_langchain()
        code_content=process_uploaded_file(uploaded_file,llm_chain)
        question = st.text_input("How do you need help with your Python code?")

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
    
    load_home_button(current_state)
    
    return

def initialize_langchain(template=None):
    ''' intiate langchain thing (fill this in bc tbh idk wtf this is i havent been to class lol)

    Paramters
    ---------
    template:str, default="""\nYou are an expert Python developer helping a user improve their code.\n A user has uploaded the following Python sample: \n{code_content}\n The user asked: "{question}"\nPlease provide suggestions for improving code quality, readability, and efficiency. Please determine any bugs and provide a revised version of the code with comments."""
        While we already have our own prompt built in, anyone interested in prompt engineering can go ahead and use
        their own prompts and replace although this still has to be fully implemented
        

    Returns
    -------
    None


    Notes
    -----


    Examples
    --------


    '''
    template=template if template is not None else """
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
    return llm_chain

def process_uploaded_file(uploaded_file,llmchain=initialize_langchain()):
    ''' process the uploaded file and give the option to return to the homescreen
    Parameters
    ----------
    uploaded_file:st.file_uploader,default=st.file_uploader
        The file your uploading im lazy and will fill this in later

    llm_chain:RunnableSequence, default=initialize_langchain()
      A LangChain pipeline that takes input matching the PromptTemplate and passes it through the ChatOpenAI model
      By default we just call the function so it uses a langchain but I wrote the steps out more discretely than that
      so that we could tell



    Returns
    -------
    Code content:str,default=code_bytes.decode("utf-8")
        The literal content of the code that was provided. This was mostly provided as a form of neatness honestly
        streamlit is just kind of simaltaneously tacky and useful all at once.



    Examples
    --------



    Notes
    -----
    Basically just so its neater lol

    '''
    code_bytes = uploaded_file.read()
    code_content = code_bytes.decode("utf-8")

    st.subheader("Code Preview")
    st.code(code_content, language="python")
    st.write(f"Your script has {len(code_content.splitlines())} lines of code.")


    if st.checkbox("Show raw code text"):
        st.text(code_content)

    return code_content

if __name__=='__main__':
 '''   print("yessir its working!")

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
                    st.error(f"Error running code: {e}")'''