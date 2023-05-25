import streamlit as st


def prompt_generator(Recruiter_Name=None, Company_Name=None, My_Name=None, My_Work_Ex=None, Application_Role=None, additional_prompts=""):
    prompt = f""" 

Pretend you are a data scientist reaching out to a recruiter via a Linkedin inmail. Based on the details below draft a personalized inmail.

1. My name: {My_Name}

2. Recruiter Name: {Recruiter_Name}

3. Company I am applying for: {Company_Name}

4. Role I am applying for: {Application_Role}

5. {My_Work_Ex}

6. Be mindful to not use buzzwords again and again and make it comprehensible and easy to read. 

7. Make it short and not too long. Don't include the subject line. Don't be overly formal.

8. Ask for connecting further.

"""

    return prompt