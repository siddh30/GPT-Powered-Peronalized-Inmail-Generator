import streamlit as st
from helpers.work_ex_functions import work_ex_form, work_ex_from_df
import pandas as pd

#### SIDEBAR ####

def sidebar():
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
        return api_key, option
    


#### Main Page Class
class MainPage():

    def __init__(self, api_key, option):
        self.api_key = api_key
        self.option =  option


    def personal_info_form(self,option):
        st.caption("1. Enter Your Profile!")
        #### To build a DataFrame from a form
        work_ex_form()

        #### Get workex_propmt from dataframe
        work_ex_from_df(option)


    def upload_presaved_csv(self, option):
        st.caption("1. Enter a pre-saved file having your information")
        uploaded_file = st.file_uploader("Upload file")

        #### To build a DataFrame from an unploaded form
        if uploaded_file is not None:
            st.session_state['df1'] = pd.read_csv(uploaded_file)

         #### Get worex_propmt from dataframe
        if 'df1' in st.session_state:
            df = st.session_state['df1']
            st.text('')
            st.caption("Summary of the Work Experiences you have added. You can always add more!")
            st.dataframe(df)
            work_ex_from_df(option)

   
    def recruiter_info(self, option):
        st.caption("2. Enter Recruiter Information")
        col1, col2 = st.columns(2)
        if option == 'Start here!':
            key = 1

            if f'Recruiter{key}' not in st.session_state:
                st.session_state[f'Recruiter{key}'] = {}
           

        else:
            key = 2
            
            if f'Recruiter{key}' not in st.session_state:
                st.session_state[f'Recruiter{key}'] = {}
           

        with col1:
            if 'Recruiter_Name' in st.session_state[f'Recruiter{key}']:
                name_value =  st.session_state[f'Recruiter{key}']['Recruiter_Name']
            else:
                name_value = ""
            st.session_state[f'Recruiter{key}']['Recruiter_Name'] = st.text_input("Recruiter Name", key=f'Recruiter_Name_text{key}',value=name_value)
        
        with col2:
            if 'Recruiter_company' in st.session_state[f'Recruiter{key}']:
                company_value =  st.session_state[f'Recruiter{key}']['Recruiter_company']
            else:
                company_value = ""
            st.session_state[f'Recruiter{key}']['Recruiter_company'] = st.text_input("Recruiter Company",key=f'Recruiter_Company_text{key}',value=company_value)
        
            
            
            




