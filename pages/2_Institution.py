import streamlit as st 
import matplotlib.pyplot as plt 
import pickle as pkl 
import streamlit_authenticator as stauth
import pandas as pd
import bz2file as bz 
import time


data = bz.BZ2File('model.pbz2', 'rb')
pipe = pkl.load(data)

st.set_page_config(page_icon="icon/staffs.png",page_title="Institution",layout="wide")

import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


style = """
<style>
    #login{
        text-align: center;
    }
    .css-12ttj6m.epcbefy1{
        border:none;
    }

    .row-widget.stButton{
        display:flex;
        justify-content:center;
        align-item:center;
    }

    .edgvbvh5{
        align-item:center;
        width:360px;
        margin-top:15px;
        border-radius: 8px;
        font-weight:500px;
        background-color:#19376D;
        color:#fff;
        transition:0.5s ease-in-out;
    }
    .edgvbvh5:hover{
        width:360px;
        margin-top:15px;
        border-radius: 8px;
        font-weight:500px;
        background-color:#19376D;
        color:#A5D7E8;
        transition:0.5s ease-in-out;
        font-weight:700;
    }
    .edgvbvh5:focus(not{
        width:360px;
        margin-top:15px;
        border-radius: 8px;
        font-weight:500px;
        color:#A5D7E8;
        background-color:#19376D;
        font-weight:600;
    }
</style>
"""

st.markdown(f"{style}",unsafe_allow_html=True)

name, authentication_status, username = authenticator.login("Login","main")

if authentication_status == False:
    login_unsucess = """
        <style>
            .block-container.css-z5fcl4.egzxvld4{
                width: 550px;
                display:flex;
                justify-content:center;
                align-item:center;
            }
        </style>
    """
    st.markdown(f"{login_unsucess}",unsafe_allow_html=True)

    st.error("Username / Password is Incorrect...")


if authentication_status == None:
    st.warning("Please enter your username and password...")

    login_unsucess = """
        <style>
            .block-container.css-z5fcl4.egzxvld4{
                width: 550px;
                display:flex;
                justify-content:center;
                align-item:center;
            }
        </style>
    """
    st.markdown(f"{login_unsucess}",unsafe_allow_html=True)

if authentication_status == True:
    st.title("Institution Login")

    login_sucess = """
        <style>
            .block-container.egzxvld4{
                width: 100%;
                display:flex;
                justify-content:center;
                align-item:center;
            }
        </style>
    """
    st.markdown(f"{login_sucess}",unsafe_allow_html=True)

    with st.sidebar:
        sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:center;
                }
            </style>
        """
        st.markdown(f"{sty}",unsafe_allow_html=True)
        if name == 'Test':
            st.subheader("Test login")

        else:
            st.subheader(f"Welcome {name}")

    authenticator.logout("Logout",'sidebar')


    f = st.file_uploader(label="Upload students data :",type="CSV",accept_multiple_files=False)
    st.info("Note : The data should be in the following format...⤵",)
    df_demo = pd.DataFrame(
        {
        'Hours_Study':[2, 2, 6, 1, 3],
        'Hours_Entertainment':[2, 6, 7, 5, 7],
        'IAT_Marks':[80, 68, 56, 50, 94],
        'Attendance_Percentage':[84, 96, 91, 97, 80]
        }
    )
    st.table(df_demo)
    if st.button(" Submit "):
        my_bar = st.progress(0, text="Prediction is going on...")

        
        
        try:
            df = pd.read_csv(f)
            y_pred = pipe.predict(df)
            
            df['predicted_value'] = y_pred
            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1, text="Prediction is going on...")
            time.sleep(0.5)

            my_bar.empty()
            df['predicted_value']=df['predicted_value'].map({1:"Pass",0:"Fail"})
            st.subheader("Output")
            st.table(df)
            @st.cache_data
            def convert_df(df):
                return df.to_csv().encode('utf-8')
            csv = convert_df(df)
            st.download_button( 
                label="Download data as CSV",
                data=csv,
                file_name='sample_df.csv',
                mime='text/csv',
            )
        except:
            my_bar.empty()
            st.error("ERROR : The given file doesn't follow the format.")
