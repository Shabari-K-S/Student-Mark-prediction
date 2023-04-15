import streamlit as st 
import pandas as pd

st.set_page_config(page_title='Contibute',page_icon='icon/contri.png',layout = 'wide')

def contribution_page():
    st.header("Contribute data to our Project")
    
    # Add some CSS to style the form
    st.markdown(
        """
        <style>
        .stTextInput > div > input {
            background-color: #f5f5f5;
            border: none;
            padding: 8px;
            margin-bottom: 20px;
            width: 100%;
            border-radius: 5px;
        }
        
        .stTextArea > div > textarea {
            background-color: #f5f5f5;
            border: none;
            padding: 8px;
            margin-bottom: 20px;
            width: 100%;
            border-radius: 5px;
            resize: none;
            height: 150px;
        }
        
        .submitButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        .submitButton:hover {
            background-color: #3e8e41;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Create form for contributions
    with st.form("contribution_form"):
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        c1,c2,c3 = st.columns([3,1,3])

        with c1:
            iat_1 = st.number_input("Enter your IAT-1 marks :",min_value=0,max_value=100)

            hos = st.number_input("Hours spent for studying : ",min_value=0,max_value=8)
        with c3:
            iat_2 = st.number_input("Enter your IAT-2 marks :",min_value=0,max_value=100)

            hoe = st.number_input("Hours spent for entertainment : ",min_value=0,max_value=8)

        attendence = st.slider("Your Attendence Precentage : ",min_value=0,max_value=100)
            
        # Add CSS class to submit button
        submit_button = st.form_submit_button(label="Submit")
        
        if name!="" and email!="": 
            if submit_button:
                data = {"Name": [name], "Email": [email], "IAT": [int((iat_1+iat_2)/2)], "Hours_studied" : hos,"Hours_entertained" : hoe,"Attendence": attendence}
                df = pd.DataFrame(data)
                st.success("Thank you for your contribution!")
                st.table(df)
        else:
            st.warning("Enter your Name and Email address")






contribution_page()
