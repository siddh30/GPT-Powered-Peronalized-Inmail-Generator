
def prompt_generator(Recruiter_Name=None, Comapny_Name=None, My_Name=None, Application_Role=None, additional_prompts=""):
    prompt = f""" 

    Pretend you are a data scientist reaching out to a recruiter via a Linkedin inmail. Based on the details below draft a personalized inmail.

    - Recruiter Name: {Recruiter_Name}
    - Company Name: {Comapny_Name}
    - My name: {My_Name}
    - Role I am applying for: {Application_Role}


    - My Work Experiences :

    1) Cognizant - Data Scientist
    Pharmaceutical Client - External
    • Built, trained, and evaluated TensorFlow models in Python for predicting the presence of ‘Crows Feet’ for subject images using Transfer Learning (such as InceptionV3 and VGG16) which achieved accuracies (AUC) of 95%
    • Analyzed data to check distribution and misclassifications on subjects of different ages, genders, and Fitzpatrick Skin Types under standard and Parallel Polarized Lighting.
    • Presented results to client executives and senior leadership in the medical team and proposed integration and deployment strategies for treatment automation of facial aesthetics.
    Cognizant Life Sciences - Internal
    • Built an NLP - based web app to carry out a Medical Legal Review (MLR) of drugs which helped secure a partnership deal with a multinational pharmaceutical client.
    • Added ‘Object Character Recognition feature to read and understand claims on various drugs from a pdf, jpeg poster, or a text document and applied smart business rules to accelerate MLR and increase FDA approvals by 30%.

    2) Stevens Institute of Technology -  ECE Summer Honors Researcher
    • Spearheaded research on Industrial Recommender Systems implemented by organizations such as YouTube, Spotify, and Netflix in real time.
    • Designed machine learning algorithms to generate the most relevant and meaningful media recommendations for users based on ratings, comments, etc.
    • Summarized findings to professors and directors of Artificial Intelligence at Stevens and was selected as a Guest Alumni Speaker for a professional development workshop hosted by the ECE department.

    - Be mindful to not use buzzwords again and again and make it comprehensible and easy to read. 

    - Make it short and not too long. Don't include the subject line. Don't be overly formal.

    - Ask for connecting further.

    - {additional_prompts}

    """

    return prompt