# Import Packages
import os
import io
import contextlib
from dotenv import load_dotenv
import streamlit as st
from streamlit_ace import st_ace
from utilities import load_home_button, load_openai_API
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Load environment variables
load_dotenv('/Users/luisperez/Desktop/AI_Tools/envfile.env')
openai_api_key = os.getenv("OPENAI_API_KEY")
print("KEY LOADED:", openai_api_key)

def run_code_improver(current_state):
    current_state = current_state if current_state is not None else st.session_state
    st.title("Python Code Assistant")

    if 'file_code_dataset' in current_state and current_state.file_code_dataset is not None:
        load_openai_API()
        uploaded_file = current_state.file_code_dataset
        embedding_model = OpenAIEmbeddings()
        vectorstore = FAISS.load_local("output/faiss_index_script", embeddings=embedding_model)

    uploaded_file = st.file_uploader("Upload your Python script", type="py")

    if uploaded_file:
        if 'file_code_dataset' in current_state and current_state.file_code_dataset is not None:
            improve_code_RAG(uploaded_file, current_state)
            return

        improve_code(uploaded_file)

    load_home_button(current_state)
    return

def improve_code_RAG(uploaded_file, current_state):
    load_openai_API()
    embedding_model = OpenAIEmbeddings()
    vectorstore = FAISS.load_local("output/faiss_index_script", embeddings=embedding_model)

    llm_chain = initialize_langchain(mode="rag")
    question = st.text_input("How do you need help with your Python code?")

    if question and st.button("Suggest Improvements"):
        results = vectorstore.similarity_search(question, k=3)
        context = "\n\n".join([doc.page_content for doc in results])

        with st.spinner("Analyzing your code..."):
            result = llm_chain.invoke({
                "code_context": context,
                "question": question
            })

        output_text = result.content if hasattr(result, "content") else result
        st.markdown("Suggestions & Improvements")
        st.markdown(output_text if output_text else "*No response received from LLM*")
        st.session_state.generated_code = output_text

        show_and_run_code_editor(output_text)

    return

def improve_code(uploaded_file):
    llm_chain = initialize_langchain(mode="regular")
    code_content = process_uploaded_file(uploaded_file)

    question = st.text_input("How do you need help with your Python code?")

    if question and st.button("Suggest Improvements"):
        with st.spinner("Analyzing your code..."):
            result = llm_chain.invoke({
                "code_content": code_content,
                "question": question
            })

        output_text = result.content if hasattr(result, "content") else result
        st.markdown("Suggestions & Improvements")
        st.markdown(output_text if output_text else "*No response received from LLM*")
        st.session_state.generated_code = output_text

        show_and_run_code_editor(output_text)

    return

def initialize_langchain(mode="regular", template=None):
    if mode == "rag":
        template = template if template is not None else """
        You are an expert Python developer helping a user improve their code.
        Based on the following relevant code context retrieved from a vector search:

        {code_context}

        The user asked: "{question}"

        Please provide helpful suggestions for improving code quality, readability, and efficiency.
        If you detect any bugs, explain them and provide a revised version of the code with comments.
        """
        input_vars = ["code_context", "question"]
    else:
        template = template if template is not None else """
        You are an expert Python developer helping a user improve their code.
        A user has uploaded the following Python sample:

        {code_content}

        The user asked: "{question}"

        Please provide suggestions for improving code quality, readability, and efficiency.
        Please determine any bugs and provide a revised version of the code with comments.
        """
        input_vars = ["code_content", "question"]

    prompt = PromptTemplate(input_variables=input_vars, template=template)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm_chain = prompt | llm
    return llm_chain

def process_uploaded_file(uploaded_file):
    code_bytes = uploaded_file.read()
    code_content = code_bytes.decode("utf-8")

    st.subheader("Code Preview")
    st.code(code_content, language="python")
    st.write(f"Your script has {len(code_content.splitlines())} lines of code.")

    if st.checkbox("Show raw code text"):
        st.text(code_content)

    return code_content

def show_and_run_code_editor(code_text):
    st.subheader("Edit Suggested Code")
    edited_code = st_ace(value=code_text, language='python', theme='monokai', key='ace-editor')
    st.session_state.cleaned_code = edited_code

    if st.button("Run Edited Code"):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                exec(st.session_state.cleaned_code, {})
                output = f.getvalue()
                st.success("Code ran successfully!")
                st.text(output)
            except Exception as e:
                st.error(f"Error running code: {e}")
