# qac-387-assignment-3


# Python Code Assistant 
This project builds an AI powered "Homework Station App" using LangChain, OpenAI, and Streamlit. The tool includes a couple different small "homework" station tools. The user can use curated LLM's to either improve their code or run data analysis tasks. A nifty side component
is the ability to get spotify music suggestions


# Installation
In order to run our app you need various dependencies which can be found in the requirements.txt. The easiest way to set this up yourself is to just run our startup "bootstrap" files included for both Mac users with bash shells as well as windows users with powershells. 
 

```shell

#Mac
bash ./bootstrap_mac.sh

#Windows
powershell -ExecutionPolicy Bypass -File .\bootstrap_win.ps1

```

Theese files are set up in such a way that they will create a virtual environment that can then be activated anytime you would like to run the app. They display an example on how to activate it but for the users convenience we also provide it here:

```shell

#Mac
bash ./bootstrap_mac.sh

#Windows
Write-Host "`n✓ Environment ready!  Next time run:`n    & .\.venv\Scripts\Activate.ps1"

```

If you would rather just pip install the requirements yourself and are familiar with the process this works as well.


# Running The App
In order to run our app you currently need to run using streamlits method as we have not yet pushed it onto streamlits open-hosting platform.

```bash
streamlit run homework_helper/Homescreen.py
```

# A note on the code editor

The code editor currently runs live editable code via streamlit-ace but, it often does not run very well as paths need to be adjusted and not a lot of error checking has been built in. This is mainly meant to be a conceptual representation added towards the end of the project and more work would be done on it in order to get it fully functional.

# A note on the music curator

At the moment, the music curator runs on our personal developer accounts because we need to be offically approved by the spotify team as an "app" in order so that we may be able to sync to anyone's account as well
as access music features.

This was worked around by using the 1 million songs dataset on kaggle here:

-['https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs'] 

We pre-processed the music dataset in order to to be able to provide suggestions without there being need for feature extraction via spotifys API but, this does limit any requests to be within the scope of the music included in the dataset mentioned above. We are also including a screen recording example of how the spotify music player would work as an aspect of the app once we are able to access both song-features and connect to various user accounts via API. 

-['']

The last note on the music curator is 

