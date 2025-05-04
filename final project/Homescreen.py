import streamlit as st
from code_improver import run_code_improver
from music_curator import run_music_picker

# Initialize 'page' in session_state if it doesn't exist yet
if 'page' not in st.session_state:
    st.session_state.page = None

# Intro screen
if st.session_state.page is None:
    st.title("Welcome to your personal homework station!")
    st.subheader("What would you like to do today?")
    

# Buttons on home screen, only displayed if no page is selected
if st.session_state.page is None:
    button_work_music = st.button("Pick some songs out for my work session")
    button_data_analysis = st.button("Lets get to some data analysis!")
    button_improve_my_code = st.button("Can you help me improve my code?")

    # Using session_state to track the screen selection
    if button_work_music:
        st.session_state.page = 'work_music'
    elif button_data_analysis:
        st.session_state.page = 'data_analysis'
    elif button_improve_my_code:
        st.session_state.page = 'improve_code'

    # Use the `st.experimental_rerun()` to immediately refresh the page
    if st.session_state.page:
        st.rerun()

# Run various modules based on if we actually have our stuff picked out or not
if st.session_state.page == 'work_music':
    run_music_picker(st.session_state)
    

elif st.session_state.page == 'data_analysis':
    st.subheader("Data Analysis")
    st.file_uploader(label="Upload your file here!")
    

elif st.session_state.page == 'improve_code':
    st.subheader("Improve your code")
    run_code_improver(st.session_state)

    


    
    
