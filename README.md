# qac-387-assignment-3


# Python Code Assistant 
This project builds an AI powered "Homework Station App" using LangChain, OpenAI, and Streamlit. The tool includes a couple different small "homework" station tools. The user can use curated LLM's to either improve their code or run data analysis tasks. A nifty side component
is the ability to get spotify music suggestions

# Running the app
In order to run our app you currently need to run using streamlits method as we have not yet pushed it onto streamlits open-hosting platform.

```bash
streamlit run homework_helper/Homescreen.py
```

# Installation
In order to run our app you need various dependencies which can be found in the requirements.txt. The easiest way to try this out is to just
create python virtual environemtn yourself and pip install from our requirements file which we include below.


```bash

#Mac
cp .env.example .env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#Windows
copy .env.example .env

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.
