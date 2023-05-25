
import pandas as pd
from helpers.chat_prompts import prompt_generator
import streamlit as st
from helpers.work_ex import work_ex_form, work_ex_from_df, work_ex_pipeline
from helpers.generator import PromptReplyGenerator


### Intailize Variables
reply = None
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
    option = st.radio("Choose Input option", ['Start here!', 'Use a pre-saved csv file!'])




##### MAIN PAGE #######
if api_key:
    
        ##### Row 1
        if option== 'Start here!':
            st.caption("1. Enter Your Profile!")
            work_ex_pipeline()

        else:
            st.caption("1. Enter a pre-saved file having your information")
            uploaded_file = st.file_uploader("Upload file")
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                st.session_state['df1'] = df
                
            if 'df1' in st.session_state:
                df =  st.session_state['df1']
                st.text('')
                st.caption("Summary of the Work Experiences you have added. You can always add more!")
                st.dataframe(df)

                work_ex_from_df(df)

    

        #### Row 2
        if (option== 'Start here!' and 'workex' in st.session_state):
            st.caption("2. Enter Recruiter Information")
            col1, col2 = st.columns(2)

            with col1:
                st.session_state['Recruiter_Name1'] = st.text_input("Recruiter Name", key=0)
                

            with col2:
                st.session_state['Recruiter_company1'] = st.text_input("Recruiter Company", key=1)
                

            if ('Recruiter_company1' in st.session_state) and ('Recruiter_Name1' in st.session_state):
            
                PromptReplyGenerator(api_key, prompt_generator=prompt_generator, Recruiter_Name=st.session_state['Recruiter_Name1'], Recruiter_Company=st.session_state['Recruiter_company1'])
                if 'reply' in st.session_state:
                    st.success(st.session_state['reply'])
                    col1, col2, _ = st.columns(3)
                    
                    with col2:
                        st.download_button("Save GPT reply!", st.session_state['reply'], file_name="Inmail.txt", use_container_width=True)

            
        elif (option=='Use a pre-saved csv file!'):
            st.caption("2. Enter Recruiter Information")
            col1, col2 = st.columns(2)

            with col1:
                st.session_state['Recruiter_Name2'] = st.text_input("Recruiter Name",key=3, )
                st.text(st.session_state['Recruiter_Name1'])
                st.text(st.session_state['Recruiter_Name2'])
            
            with col2:
                st.session_state['Recruiter_company2'] = st.text_input("Recruiter Company",key=4)

            if ('Recruiter_company2' in st.session_state) and ('Recruiter_Name2' in st.session_state):

                PromptReplyGenerator(api_key, prompt_generator=prompt_generator, Recruiter_Name=st.session_state['Recruiter_Name2'], Recruiter_Company=st.session_state['Recruiter_company2'])
                if 'reply' in st.session_state:
                    st.success(st.session_state['reply'])
                    col1, col2, _ = st.columns(3)
                    
                    with col2:
                        st.download_button("Save GPT reply!", st.session_state['reply'], file_name="Inmail.txt", use_container_width=True)


else:
    st.markdown("Please Enter your ***Open AI account API*** in the siderbar to proceed!")


