# Python Code Assistant 

This project builds an AI-powered "Homework Station App" using LangChain, OpenAI, and Streamlit. The idea is to have a workspace similar to the one provided by [https://www.notion.com/] with LLM tools that facilitate curation.

Since this was a class project we began small, and the two main tools leveraged are:

RAG pipelines with Facebook's FAISS for efficient vector search in order to create a personalized user experience that improves over time. In theory, the more you use your assistant for a specific kind of task, the better it gets at your personalized workflow. Over the course of a major project, you would begin to have an assistant with personalized insight and suggestions on where things may be going wrong or could be improved.

The OpenAI embeddings module is also leveraged to create embeddings of song features for efficient clustering and song suggestions. While a smaller component in the preliminary exploration, the lag time for clustering our initial large dataset was a bit unreasonable. But if you were pulling only 200–500-ish songs from a user's history and ran the same process, it would be much more reasonable. In effect, batching would help—but further access to Spotify’s API is necessary.

While this is a preliminary exploration for a class project, we do come away with a few major results:

FAISS and vector storage actually provide an amazing way to personalize a model for your use case and have various applications that would involve using the code shown in this project and simply switching out prompts and tasks.

Connecting this same pipeline to outside APIs, such as Spotify’s, in order to implement those as outside databases in the RAG pipeline is actually a relatively easy implementation and points to the exciting breadth of possibilities for the future.

These results lay the foundations for the key takeaways from this project:

## Key takeaways?: 


- Building an app is actually a very approachable, scalable, and fun time. Data is the future, LLMs are easier to implement, curate, and use than ever, and we have definitely come away with a very valuable skill set.

## Lessons learned?:

- UI work, CSS, and web apps are still hard to use

- If this were a real product pitch, editing before presenting is essential—and sometimes you have to know when to put the thing down

- Collaboration is key; aspects of other presentations made their way into our final product. Market research earlier would have been useful

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

