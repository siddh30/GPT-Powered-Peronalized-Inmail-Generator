import openai
from chat_prompts import prompt_generator
import streamlit as st

### Intailize Variables
confirmation = None


st.title("Personalized LinkedIn Inmail")

#### SIDEBAR ####

with st.sidebar:
    
    _,col2,_ = st.columns(3)
    
    with col2:
        st.caption("Powered By -")

    st.image("./images/logo.jpg")


    with st.expander("Model Details"):
        st.markdown("Model - gpt 3.5 turbo")
        st.markdown("Expense - $0.002 per 1K tokens")


    api_key = st.text_input("Enter your API Key!", type='password')
    st.caption("Your API key will not be saved!")


    option = st.radio("Choose Input option", ['Start here!', 'Use a pre-saved text file!'])


##### Main Page

if api_key:

    if option == 'Start here!':

        col1, col2 = st.columns(2)

        with col1:
            My_Name = st.text_input("Enter Your Name")

        with col2:
            Application_Role = st.text_input("Role you are applying to!")
            
        if My_Name and Application_Role:

            col1, col2 = st.columns(2)
            
            with col1:
                Recruiter_Name = st.text_input("Recruiter Name")

            with col2:
                Recruiter_Company = st.text_input("Recruiter Company")

            if Recruiter_Company and Recruiter_Name:
                st.text("")
                confirmation = st.button("Submit These Choices")
                st.caption("Charges apply on token generation!")



        if confirmation:
            prompt =  prompt_generator(My_Name=My_Name, Application_Role=Application_Role, Recruiter_Name=Recruiter_Name, Comapny_Name=Recruiter_Company)
            # st.text(prompt)

            try:
                openai.api_key = api_key
                messages = [
                    {"role": "system", "content": prompt},
                ]
                    
                chat = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo", messages=messages
                        )
                reply = chat.choices[0].message.content

                st.success(reply)


            except: 
                st.error("Oops! we were unable to run your request. Please check the following: -")
                st.markdown("- Ensure your Open AI acount has your billing information!")
                st.markdown("- Please check your API key!")
                st.markdown("- If you have used a presaved text file, please check that it follows the right format!")


else:
    st.markdown("Please Enter your ***Open AI account API*** in the siderbar to proceed!")

