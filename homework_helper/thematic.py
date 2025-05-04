import streamlit as st
'''some commenting for me about css
-citations here would go to chatgpt i didnt really put the effort in to look much up for this beta app other than
the flow of streamlit logic

So since we are rendering as a web-app we can use CSS to inject style directly into stuff
-.stAPP-> our main "container" (I imagine this is closest to an object in python, russion doll-esque information distribution)
-button->selects 
-[data-testid="stSidebar"]->sidebar
-h1, h2, h3->headers

after that its case-specific parameters for various aesthetics
per say
-font family:'font'=setting a font

there is an example list below but really this is a great chance for gpt to just automate aesthetics

'''


######################################################################################################
#This is an example of how to do the css
#st.markdown(
#    """
#    <style>
#    /* Change the entire app font */
#    .stApp { 
#        font-family: 'Arial', sans-serif;
#        font-size: 16px;
#        color: #333333;
#    }
#
#    /* Change all buttons */
#    button {
#        font-family: 'Arial', sans-serif !important;
#        font-size: 16px !important;
#    }
#
#    /* Change sidebar fonts */
#    [data-testid="stSidebar"] {
#        font-family: 'Arial', sans-serif;
#        font-size: 16px;
#    }
#
#    /* Optional: Change headers */
#    h1, h2, h3, h4, h5, h6 {
#        font-family: 'Arial', sans-serif;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True
#)
######################################################################################################

def set_theme(
    background_color='#72fff3',
    font_family='Futura, Fantasy',
    app_font_size='20px',
    text_color='#f4ecf7',
    button_font_size='16px',
    sidebar_font_size='16px',
    header_color='#f4ecf7',
    button_background_color='#72fff3',
    button_text_color='#000000',
    button_border_color='#ffffff',
    button_hover_background='#4DB6AC',
    button_hover_text='#ffffff'
):
    '''
    Set customizable theme colors and styles for the app.

    Parameters
    ----------
    background_color : str
        Background color for the app (CSS color code).
    font_family : str
        Font family for the app.
    app_font_size : str
        Main app font size.
    text_color : str
        Default text color.
    button_font_size : str
        Font size for buttons.
    sidebar_font_size : str
        Font size for sidebar.
    header_color : str
        Color for headers (h1-h6).
    button_background_color : str
        Background color for buttons.
    button_text_color : str
        Text color for buttons.
    button_border_color : str
        Border color for buttons.
    button_hover_background : str
        Background color when hovering over buttons.
    button_hover_text : str
        Text color when hovering over buttons.

    Returns
    -------
    None
    '''

    import streamlit as st

    st.markdown(
    f"""
    <style>
    /* Entire app */
    .stApp {{
        background-color: {background_color} !important;
        font-family: {font_family} !important;
        font-size: {app_font_size} !important;
        color: {text_color} !important;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        font-family: {font_family} !important;
        font-size: {sidebar_font_size} !important;
        color: {text_color} !important;
    }}

    /* Markdown container text */
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span {{
        font-family: {font_family} !important;
        font-size: {app_font_size} !important;
        color: {text_color} !important;
    }}

    /* File uploader label */
    [data-testid="stFileUploaderLabel"] {{
        font-family: {font_family} !important;
        font-size: {app_font_size} !important;
        color: {text_color} !important;
    }}

    /* Buttons */
    button[data-testid="baseButton"] {{
        background-color: {button_background_color} !important;
        color: {button_text_color} !important;
        border: 1px solid {button_border_color} !important;
        font-family: {font_family} !important;
        font-size: {button_font_size} !important;
        border-radius: 8px !important;
        padding: 0.5em 1em !important;
    }}

    button[data-testid="baseButton"]:hover {{
        background-color: {button_hover_background} !important;
        color: {button_hover_text} !important;
    }}

    /* Headers */
    h1, h2, h3, h4, h5, h6 {{
        font-family: {font_family} !important;
        color: {header_color} !important;
    }}

    /* stElementContainer inner blocks (if desired) */
    [data-testid="stElementContainer"] > div {{
        background-color: {button_hover_background} !important;
        padding: 10px !important;
        border-radius: 10px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


