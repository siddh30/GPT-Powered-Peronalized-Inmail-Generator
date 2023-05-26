
import pandas as pd
from helpers.chat_prompts import prompt_generator
import streamlit as st
# from helpers.work_ex_functions import work_ex_form, work_ex_from_df, work_ex_pipeline
from helpers.generator import PromptReplyGenerator
from elements import sidebar, MainPage



            
### Title
st.title("Personalized LinkedIn Inmail")

#### SIDEBAR ####
api_key, option = sidebar()
main_page = MainPage(api_key, option)



##### MAIN PAGE #######
if api_key:
    
    if option== 'Start here!':
        key = 1
        df_key = 'df'
        workex_key = 'workex'
        reply_key = 'reply'
        prompt_key = 'prompt'

        main_page.personal_info_form(option)

    else:
        key=2
        main_page.upload_presaved_csv(option)
        df_key = 'df1'
        workex_key = 'workex1'
        reply_key = 'reply1'
        prompt_key = 'prompt1'


       
    if df_key in st.session_state:
                main_page.recruiter_info(option)
                kwargs = {'api_key':api_key, 'Recruiter_Name': st.session_state[f'Recruiter{key}']['Recruiter_Name'],
                        'Recruiter_Company': st.session_state[f'Recruiter{key}']['Recruiter_company'],
                        'prompt_generator':prompt_generator,'df_key':df_key, 'workex_key':workex_key, 
                        'reply_key':reply_key, 'prompt_key' : prompt_key}
    
                PromptReplyGenerator(**kwargs)

    
else:
    st.markdown("Please Enter your ***Open AI account API*** in the siderbar to proceed!")


