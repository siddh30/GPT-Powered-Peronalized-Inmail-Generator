import streamlit as st
import pandas as pd

def work_ex_from_df(option):
    if option == 'Start here!':
        key ='df'
        key1 = 'workex'

    else:
        key = 'df1'
        key1 = 'workex1'
     
    if key in st.session_state:
        df =  st.session_state[key]

        newline = f"""\n\n"""
        result = f"""My Work Experiences:-"""
        for i in range(len(df)):
            c = df['Company Name'].iloc[i]
            r = df['Role'].iloc[i]
            t = df['Time'].iloc[i]
            d = df['Description'].iloc[i]
            work_ex = (f"""{newline}Company {i+1} - {c}{newline}Role - {r}{newline}Time - {t}{newline}Description - {d}""")
            result += f"{work_ex}{newline}"

        st.session_state[key1] = result


def work_ex_form():
    if 'work_exp_dict' not in st.session_state:
        st.session_state['work_exp_dict'] = {}


    with st.expander("Fill out this form!", expanded=True):
                
                    col1, col2 = st.columns(2)

                    #### Name 
                    with col1:

                        if 'My Name' in st.session_state['work_exp_dict']:
                            my_name_value = st.session_state['work_exp_dict']['My Name']
                            
                        else:
                            my_name_value = ""
                            

                        My_Name = st.text_input("What is your name?",value=my_name_value)
                        st.session_state['work_exp_dict']['My Name'] = My_Name
                    
                    ### Application Role
                    with col2:

                        if 'Application Role' in st.session_state['work_exp_dict']:
                            my_application_value = st.session_state['work_exp_dict']['Application Role']
                           

                        else:
                            my_application_value = ""

                        Application_Role = st.text_input("What role are applying to?", value=my_application_value)
                        st.session_state['work_exp_dict']['Application Role'] = Application_Role



                    ### Company Name, Role, Time Worked and Descripion

                    st.caption("Your Work Experience")
                    col1, col2, col3 = st.columns(3)

                    with col1:

                        if 'Company Name' in st.session_state['work_exp_dict']:
                             c_value = st.session_state['work_exp_dict']['Company Name'][-1]
                        else:
                             c_value =''
                        a = st.text_input("Where do you work?",value=c_value)


                    with col2:

                        if 'Role' in st.session_state['work_exp_dict']:
                             r_value = st.session_state['work_exp_dict']['Role'][-1]
                        else:
                             r_value =''
                        b = st.text_input("What did you work as?",value=r_value)


                        
                    with col3:

                        if 'Time' in st.session_state['work_exp_dict']:
                             t_value = st.session_state['work_exp_dict']['Time'][-1]

                        else:
                             t_value =''

                        c = st.text_input("How long did you work?", placeholder="1 month or 1 year", value=t_value)




                    if 'Description' in st.session_state['work_exp_dict']:
                        d_value = st.session_state['work_exp_dict']['Description'][-1]

                    else:
                        d_value =''


                    d  = st.text_area("Description", placeholder='Describe your achievements', value=d_value)



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

                    if 'df' in st.session_state:
                        df =  st.session_state['df']
                        st.text('')
                        st.caption("Summary of the Work Experiences you have added. You can always add more!")

                        
                        st.dataframe(df)
                        
                        csv = df.to_csv(index=False).encode('utf-8')
                        st.download_button("Download DataFrame!", data=csv, file_name="Personal_Profile.csv", key ='downloaded')




                  



