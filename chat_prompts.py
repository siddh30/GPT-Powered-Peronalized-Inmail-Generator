
def prompt_generator(Recruiter_Name=None, Comapny_Name=None, My_Name=None, My_Work_Ex=None, Application_Role=None, additional_prompts=""):
    prompt = f""" 

    Pretend you are a data scientist reaching out to a recruiter via a Linkedin inmail. Based on the details below draft a personalized inmail.

    - Recruiter Name: {Recruiter_Name}
    - Company Name: {Comapny_Name}
    - My name: {My_Name}
    - Role I am applying for: {Application_Role}


    - My Work Experiences :

    {My_Work_Ex}

    - Be mindful to not use buzzwords again and again and make it comprehensible and easy to read. 

    - Make it short and not too long. Don't include the subject line. Don't be overly formal.

    - Ask for connecting further.

    - {additional_prompts}

    """

    return prompt