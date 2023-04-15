import streamlit as st 
from streamlit_option_menu import option_menu as opt  
st.set_page_config(page_title="About",page_icon="icon/mainmenu.png",layout='wide')

sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:center;
                }
            </style>
        """
st.markdown(f"{sty}",unsafe_allow_html=True)

with st.sidebar:
    selected = opt(
        menu_title='About',
        menu_icon='body-text',
        options=['Project','Team']
    )

if selected == 'Project':
    st.write("""
## Product Perspective:
 * Our product is a prediction web app that uses machine learning algorithms to predict a student's final semester marks based on their internal marks and other relevant factors. \n
 * It will be designed to provide accurate and reliable predictions to students, teachers, and institutions. \n
 * It will be user-friendly and easy to navigate, with clear and concise instructions.\n
## Product Features:

 * Student page for entering internal marks and other details\n
 * Institution login and registration\n
 * Institution page for entering student data and generating results\n
 * Machine learning algorithms for predicting final semester marks\n
 * Consideration of previous academic performance, attendance, and other relevant factors\n
 * Clear and concise instructions for users\n
 * Ability to export results in an excel/csv file format\n

## User Classes and Characteristics:

 * Students: Students will use the app to predict their final semester marks and get an idea of their academic performance.\n
 * Teachers: Teachers will use the app to monitor their students' academic progress and take appropriate measures to improve their performance.\n
 * Administrators: Administrators will manage the app and ensure that it is running smoothly.\n

## Special Features:
 * Users will also be able to predict whether they will be placed or not.
 * Our web app will not only predict the final semester results, it can also be used to predict whether a student will get placed or not.
 * After submitting the details a mail will be generated from our side about learning resources.
 * Users can also contribute their data.
 
""")

if selected == 'Team':
    sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:left;
                }
            </style>
        """
    st.markdown(f"{sty}",unsafe_allow_html=True)
    st.title("Team Details")
    st.header("Team Description :")
    st.write("""
         * Welcome to Cipher! We are a dynamic team of visionary professionals determined to address the challenge of predicting student grades accurately. 
         * Our mission is straightforward to develop a system that provides students with reliable grade predictions to make informed decisions about their future career options.
         * Our team comprises experts from diverse fields, who will utilize data analysis techniques and creative approaches to devise innovative solutions. 
         * We value collaboration and encourage brainstorming of ideas from all team members, regardless of size or scope. 
         * Together, we can create something truly extraordinary! Let us work harmoniously towards achieving tangible results. It's time for Cipher to shine!
""")

    st.subheader("Team members : ")
    st.write("""
         * [Viyasan S - ( Team Leader )](https://www.linkedin.com/in/viyasan-sivaraj-12b14b1a4/)
         * [Shabari K S](https://www.linkedin.com/in/shabari-k-s-56421822a) 
         * [Sathyaram R](https://www.linkedin.com/in/sathyaram-r-592b66227)
    """)
