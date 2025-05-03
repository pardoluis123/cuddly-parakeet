# qac-387-assignment-3


# Updates as of 05-03-2025

working code critic, 
working music suggester, 
working homescreen navigator,
working dataframe import and incorporation,

This all needs fine-tuning, but we finally have a proper "app," and I am now going to bed. I will upload the updated tests, and the assgn4 concept which is litteraly what our music thing does when it incorporates new music it just feels very unfeasible because of how the lag time manifests when sending calls back and forth with chatgpt at this point it truly easier to reduce using PCA and cluster using K-means but I will make a fake smaller dataset to use with openai()'s embedding techniques tommorow for incorporation of the class concepts.

Basically to incorporate it im just merging the whole row of features and making it one big string and then using the openai() model to create embeddings

I am also going to upload a .mov on the main page of the git showing how it works as of tonight while I upload a fresher version tommorow.

Sorry for lack of structure in the upate :) very tired



# Python Code Assistant 

This project builds an AI powered "Python Code Assistant" using LangChain, OpenAI, and Streamlit. The tool allows the user to upload a Python file, and the tool will suggest improvements to make the code more readable/efficient. The tool will then output an improved version of the user's Python script. 


# Duplicating the .env File
To set up your environment variables, you need to duplicate the `.env.example` file and rename it to `.env`. You can do this manually or using the following terminal command:

```bash
cp .env.example .env # Linux, macOS, Git Bash, WSL
copy .env.example .env # Windows Command Prompt
```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.
