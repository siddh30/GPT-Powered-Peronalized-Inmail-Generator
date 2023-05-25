import streamlit as st
import pandas as pd

def work_ex_from_df(df):
    if ('df' in st.session_state) or ('df1' in st.session_state):
        newline = f"""\n\n"""
        result = f"""My Work Experiences:-"""
        for i in range(len(df)):
            c = df['Company Name'].iloc[i]
            r = df['Role'].iloc[i]
            t = df['Time'].iloc[i]
            d = df['Description'].iloc[i]
            work_ex = (f"""{newline}Company {i+1} - {c}{newline}Role - {r}{newline}Time - {t}{newline}Description - {d}""")
            result += f"{work_ex}{newline}"

        st.session_state['workex'] = result


def work_ex_form():
    if 'work_exp_dict' not in st.session_state:
        st.session_state['work_exp_dict'] = {}


    with st.expander("Fill out this form!", expanded=True):
                
                    col1, col2 = st.columns(2)

                    #### Name 
                    with col1:
                        My_Name = st.text_input("Enter Your Name")
                        st.session_state['work_exp_dict']['My Name'] = My_Name

                    
                    ### Application Role
                    with col2:
                        Application_Role = st.text_input("Role you are applying to!")
                        st.session_state['work_exp_dict']['Application Role'] = Application_Role


                    ### Company Name, Role, Time Worked and Descripion
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        a = st.text_input("Company Name")
                        
                    with col2:
                        b = st.text_input("Role")
                        
                    with col3:
                        c = st.text_input("Time", placeholder="1 month or 1 year")

                    d  = st.text_area("Description", placeholder='Describe your achievements')
    
                    if My_Name and Application_Role and a and b and c and d:
                        e = st.button("Submit")
    
                        if e:
                            if 'first' not in st.session_state['work_exp_dict']:
                                st.session_state['work_exp_dict']['Company Name'] = [a]
                                st.session_state['work_exp_dict']['Role']= [b]
                                st.session_state['work_exp_dict']['Time'] = [c]
                                st.session_state['work_exp_dict']['Description'] = [d]
                                st.session_state['work_exp_dict']['first'] = 0
                                
                            else:
                                st.session_state['work_exp_dict']['Company Name'].append(a)
                                st.session_state['work_exp_dict']['Role'].append(b)
                                st.session_state['work_exp_dict']['Time'].append(c)
                                st.session_state['work_exp_dict']['Description'].append(d)
                            
                            
                            df = pd.DataFrame(st.session_state['work_exp_dict'])
                            df.drop(['first'], axis=1, inplace=True)
                            df.drop_duplicates(inplace=True)
            
                            st.session_state['df'] = df

                        
         
def work_ex_pipeline():  

    work_ex_form() 

    if 'df' in st.session_state:
        df =  st.session_state['df']
        st.text('')
        st.caption("Summary of the Work Experiences you have added. You can always add more!")

        
        st.dataframe(df)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download DataFrame!", data=csv, file_name="Personal_Profile.csv", key ='downloaded')
        
    
        work_ex_from_df(st.session_state['df'])


                  



