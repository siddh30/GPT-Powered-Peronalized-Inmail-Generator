import streamlit as st
import openai

def PromptReplyGenerator(api_key, prompt_generator, Recruiter_Name=None, Recruiter_Company=None):
    st.caption("3. Confirm Your Choices and generate the Linkedin Inmail!")
    confirmation = st.button("Submit These Choices")
    st.caption("Charges apply on token generation!")
    My_Name = st.session_state['df']['My Name'].values[0]
    Application_Role = st.session_state['df']['Application Role'].values[0]

    if confirmation:
        prompt =  prompt_generator(My_Name=My_Name, Application_Role=Application_Role, My_Work_Ex = st.session_state['workex'], Recruiter_Name=Recruiter_Name, Company_Name=Recruiter_Company)
        # st.markdown(prompt)

        try:
            openai.api_key = api_key
            messages = [
                {"role": "system", "content": prompt},
            ]
                
            chat = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo", messages=messages
                    )
            reply = chat.choices[0].message.content

            if reply:
                st.session_state['reply'] = reply

            
        except: 
            st.error("Oops! we were unable to run your request. Please check the following: -")
            st.markdown("- Ensure your Open AI acount has your billing information!")
            st.markdown("- Please check your API key!")
            st.markdown("- If you have used a presaved text file, please check that it follows the right format!")
