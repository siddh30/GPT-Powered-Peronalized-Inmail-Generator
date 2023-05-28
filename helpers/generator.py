import streamlit as st
import openai

def PromptReplyGenerator(api_key, prompt_generator, Recruiter_Name=None, Recruiter_Company=None, df_key=None, workex_key=None, prompt_key = None, reply_key=None):
    st.caption("3. Confirm Your Choices and generate the Linkedin Inmail!")

    My_Name = st.session_state[df_key]['My Name'].values[0]
    Application_Role = st.session_state[df_key]['Application Role'].values[0]
    col1, col2 = st.columns(2)


    with col1:
        prompt_confirmation = st.button("Generate Final Prompt",use_container_width=True)
        st.caption("The prompt fed to GPT!")


    with col2:
        reply_confirmation = st.button("Generate GPT Reply",use_container_width=True)
        st.caption("Charges apply on token generation!")

    
    prompt =  prompt_generator(My_Name=My_Name, Application_Role=Application_Role, My_Work_Ex = st.session_state[workex_key], Recruiter_Name=Recruiter_Name, Company_Name=Recruiter_Company)

    if prompt_key not in st.session_state or prompt != st.session_state[prompt_key]:
    #     #### If the prompt does not change but the buttons are clicked (True if prompt does change)
        st.session_state[prompt_key] = prompt
    
    if prompt_confirmation:
        st.subheader("Final Prompt")
        with st.expander("Expand to read the full prompt!", expanded=True):
            st.warning(st.session_state[prompt_key])

    if reply_confirmation:
            try:
                openai.api_key = api_key
                messages = [
                    {"role": "system", "content": prompt},
                ]
                    
                chat = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo", messages=messages
                        )
                reply = chat.choices[0].message.content

                st.session_state[reply_key] = reply 

                st.subheader("GPT Generated InMail")
                with st.expander("Expand to read the InMail!", expanded=True):
                    st.success(st.session_state[reply_key])
                
            except: 
                st.error("Oops! we were unable to run your request. Please check the following: -")
                st.markdown("- Ensure your Open AI acount has your billing information!")
                st.markdown("- Please check your API key!")
                st.markdown("- If you have used a presaved text file, please check that it follows the right format!")

            

   

