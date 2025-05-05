import streamlit as st
from code_improver import run_code_improver
from music_curator import run_music_picker
from thematic import set_theme
from utilities import load_home_button

#defining the theme at the top, im sure we can make theese customizable by the user but for now its up to us 
set_theme(
    background_color='#E6E6FA',  # soft lavender
    font_family='Futura, Fantasy',
    app_font_size='20px',
    text_color='#4B3869',
    button_font_size='16px',
    sidebar_font_size='16px',
    header_color='#4B3869',
    button_background_color='#E6E6FA',
    button_text_color='##E6E6FA',
    button_border_color='#E6E6FA',
    button_hover_background='#E6E6FA',
    button_hover_text='#ffffff'
)

path_to_background='/Users/luisperez/Desktop/AI_Tools/final project/resources/lofi_youtube_girl_background_image.jpg'

# Initialize 'page' in session_state if it doesn't exist yet
if 'page' not in st.session_state:
    st.session_state.page = None

# Intro screen
if st.session_state.page is None:
    st.image(path_to_background) #including background 
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
    
    # Rag pipeline has been pulled out:
    file_music_database=st.file_uploader('Do you have any datasets, with songs and features? It wil help us provide a better curation experience!')
    file_code_dataset=st.file_uploader('Do you have any examples of the kind of scripting you need to get done? It will help us provide a better curation experience!')
    file_data_analysis_dataset=st.file_uploader('Do you have any datasets, with the kind of analyses you need to get done? It wil help us provide a better curation experience!')

    # Use the `st.experimental_rerun()` to immediately refresh the page
    if st.session_state.page:
        st.rerun()

# Music Curator
if st.session_state.page == 'work_music':
    run_music_picker(st.session_state)
    
# Code Improver
elif st.session_state.page == 'improve_code':
    st.subheader("Improve your code")
    run_code_improver(st.session_state)

#Data Analysis Assistant
elif st.session_state.page == 'data_analysis':
    st.subheader("Data Analysis")
    st.file_uploader(label="Upload your file here!")
    load_home_button(st.session_state)

    


    
    
