import streamlit as st 
from streamlit_option_menu import option_menu as opt  
import time
import bz2file as bz
import pickle as pkl
import smtplib
from email.message import EmailMessage
import random

st.set_page_config(page_title="Student Login",page_icon="icon/graduated.png",layout='wide')


sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:center;
                }
            </style>
        """
st.markdown(f"{sty}",unsafe_allow_html=True)


def pass_fun():
    skills = ["""

    Dear Student,

    I am thrilled to congratulate you on your outstanding academic performance. Your hard work, dedication, and commitment to your studies have truly paid off, and you should be proud of your achievements.

    Please explore the following websites to further develop your skills and knowledge for your future endeavors:

    Coursera: https://www.coursera.org/
    edX: https://www.edx.org/
    Khan Academy: https://www.khanacademy.org/
    Udemy: https://www.udemy.com/
    iTunesU Free Courses: https://www.apple.com/education/itunes-u/
    MIT OpenCourseWare: https://ocw.mit.edu/index.htm
    Stanford Online: https://online.stanford.edu/
    Codecademy: https://www.codecademy.com/
    ICT iitr: http://ict.iitr.ac.in/
    ICT iitk: https://www.iitk.ac.in/ict/
    NPTEL: https://nptel.ac.in/"""]
    
    books = ["""

    Dear student,

    I am thrilled to congratulate you on your outstanding academic performance. Your hard work, dedication, and commitment to your studies have truly paid off, and you should be proud of your achievements.

    As a token of appreciation for your outstanding performance, I would like to share some valuable resources with you that can help you further develop your knowledge and skills. Here are some of the best E-book sites that you can explore to gain valuable insights and learn new things:

    Project Gutenberg: https://www.gutenberg.org/
    Google Books: https://books.google.com/
    Free-eBooks.net: https://www.free-ebooks.net/
    Bookboon: https://bookboon.com/
    OpenStax: https://openstax.org/
    Archive.org: https://archive.org/
    Scribd: https://www.scribd.com/
    ManyBooks: https://manybooks.net/
    E-Books Directory: https://www.e-booksdirectory.com/ """]
    l = [skills, books]
    i= [0,1,2]
    return random.choice(l[random.choice(i)])

def fail_fun():
    Material = ["""
    Dear student,

    I wanted to take a moment to acknowledge your efforts and hard work during the recent internal exams. Despite the results not meeting your expectations, I want you believe in you and your potential to do better.

    I am confident that with the right support and resources, you will overcome this setback and achieve your goals. In this regard, I would like to share with you some online study materials and resources that can help you improve your knowledge and skills:

    Khan Academy: https://www.khanacademy.org/
    Coursera: https://www.coursera.org/
    edX: https://www.edx.org/
    MIT OpenCourseWare: https://ocw.mit.edu/index.htm
    Chegg Study: https://www.chegg.com/study
    Udacity: https://www.udacity.com/
    Clutch Prep: https://www.clutchprep.com/
    StudyBlue: https://www.studyblue.com/
    Quizlet: https://quizlet.com/
    Brightstorm: https://www.brightstorm.com/
    CSE Concepts: https://www.youtube.com/channel/UCfxI-lr-6hG8HkWjNq3COSQ
    Mechanical Engineering Concepts: https://www.youtube.com/channel/UCdKP_Y6cU8i-7m6UaekUBjA
    EEE Concepts: https://www.youtube.com/channel/UCVpmwo_XHhd4KjQmiSPJi1Q
    ECE Concepts: https://www.youtube.com/channel/UC5EHPj04l8a5W-zcZYNRJtA
    """]

    Development = ["""
    Dear student,

    I wanted to reach out and express my appreciation for your efforts and hard work during the recent internal exams, even though the results may not have been what you were hoping for. I want you to know that I'm proud of you for your dedication and commitment to your studies.

    While it may be disappointing to not have performed as well as you hoped, I believe that there are valuable lessons to be learned from this experience. With the right support and resources, you can overcome this setback and continue to grow and improve. In this regard, I would like to share with you some useful websites that offer online lectures and resources to help you develop your skills and knowledge:
    NPTEL: https://www.youtube.com/user/nptelhrd

    Gate Lectures by Ravindrababu Ravula: https://www.youtube.com/user/ravindrababuravula

    The Organic Chemistry Tutor: https://www.youtube.com/user/TheOrganicChemistryTutor

    Neso Academy: https://www.youtube.com/channel/UCkKSDblyYVIRaW802piVXVg

    MathTheBeautiful: https://www.youtube.com/channel/UCr22xikWUK2yUW4YxOKXclQ

    Engineering Made Easy: https://www.youtube.com/user/MrNakul10

    GATE Academy: https://www.youtube.com/user/TheGateAcademy

    Unacademy Engineering: https://www.youtube.com/channel/UCZKYfN-4f9Gv6A_DDNFwqZw

    Overcoming Exam fear: https://www.youtube.com/user/ExamFearVideos 
    Project Gutenberg: https://www.gutenberg.org/
    Google Books: https://books.google.com/
    Free-eBooks.net: https://www.free-ebooks.net/
    Bookboon: https://bookboon.com/
    OpenStax: https://openstax.org/
    Archive.org: https://archive.org/
    Scribd: https://www.scribd.com/
    ManyBooks: https://manybooks.net/
    E-Books Directory: https://www.e-booksdirectory.com/ """]

    l = [Material, Development]
    i= [0,1]
    return (random.choice(l[random.choice(i)]))


    


def send_mail_to_user(email,val):
    email_address = "innovatioki123@gmail.com"
    email_password = "gdhdvfvpzawdgmim"

    if val == 1:
        context = pass_fun()
        sub = "Congratulations! Our Model has predicted that you will pass in all subjects!"
    elif val == 2:
        context ="""
            Dear student,

            I am thrilled to extend my warmest congratulations on your exceptional academic performance. Your hard work, dedication, and commitment to your studies have truly paid off, and you should be proud of your achievements.

            It gives me immense pleasure to share with you some valuable resources that can help you further develop your skills and knowledge to prepare for your future endeavors. Here are some websites that you can explore to enhance your learning and gain valuable skills for your placement:

            Ambitionbox: https://www.ambitionbox.com
            AceTheInterview: https://www.acetheinterview.com/
            GeeksforGeeks: https://www.geeksforgeeks.org/
            LeetCode: https://leetcode.com/
            Gainlo: http://www.gainlo.co/
            CareerCup: https://www.careercup.com/
            CoderCareer: https://www.codercareer.com/
            InterviewUp: https://www.interviewup.com/
            InterviewBest: https://www.interviewbest.com/
            IndiaBIX: https://www.indiabix.com/
        """
        sub="Congratulations! Our Model has predicted that you will get placement offer"
    elif val == 3:
        context = """
            Dear Student,
            I wanted to take a moment to acknowledge your efforts and hard work during the recent internal exams. Despite the results not meeting your expectations, I want you believe in you and your potential to do better.

            I am confident that with the right support and resources, you will overcome this setback and achieve your goals. In this regard, I would like to share with you some online study materials and resources that can help you improve your knowledge and skills:


            Coursera: https://www.coursera.org/
            edX: https://www.edx.org/
            Khan Academy: https://www.khanacademy.org/
            Udemy: https://www.udemy.com/
            iTunesU Free Courses: https://www.apple.com/education/itunes-u/
            MIT OpenCourseWare: https://ocw.mit.edu/index.htm
            Stanford Online: https://online.stanford.edu/
            Codecademy: https://www.codecademy.com/
            ICT iitr: http://ict.iitr.ac.in/
            ICT iitk: https://www.iitk.ac.in/ict/
            NPTEL: https://nptel.ac.in/"""
        sub = " Placement Training Resources"
    else:
        context = fail_fun()
        sub = "Study Resources"

    

    # create email
    msg = EmailMessage()
    msg['Subject'] = sub
    msg['From'] = email_address
    msg['To'] = email

    

    msg.set_content(context)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)


option = ['Placement Prediction']


with st.sidebar:
    selected = opt(menu_title="Student Login",
                   options=option,
                   menu_icon="book"
                )


if selected == option[0]:
    data_2 = bz.BZ2File('model_2.pbz2', 'rb')
    pipe_2 = pkl.load(data_2)

    st.title("Placement Prediction")
    
    st.write("###")
    
    email=st.text_input("Enter your email-id :")

    c4,c5,c6 = st.columns([3,1,3])

    with c4:
        age = st.number_input("Enter your Age : ",min_value=19,max_value=30)

        st.write("###")
        option = st.selectbox(
         'Enter your stream : ',
        ('--Select--','Electronics And Communication', 'Computer Science', 'Information Technology','Mechanical','Electrical','Civil'))

        cgpa = st.number_input("Enter your CGPA: ",min_value=0,max_value=10)
    with c6:
        stream = {'Electronics And Communication':0, 'Computer Science':1,
            'Information Technology':2, 'Mechanical':3, 'Electrical':4, 'Civil':5}
        
        gender = st.selectbox(
            "Select your gender",
            ('Male', 'Female'))
        
        st.write("###")
        intern_c = st.number_input("Enter no. of Internships attended : ",min_value=0,max_value=8)

        Hostelers = st.selectbox(
            "Have you attended any placement related training before ?",
            ("Yes",'No')
        )
        
    hob = st.selectbox(
        'History Of Backlogs ? ',
        ('Yes','No')
    )

    if st.button("Submit"):
        stre = stream[option]
        if gender == 'Male':
            gen = 1
        else:
            gen = 0
        if Hostelers == "Yes":
            host = 1
        else:
            host = 0
        if hob == "Yes":
            hbl = 1
        else:
            hbl = 0

        res = pipe_2.predict([[age,gen,stre,intern_c,cgpa,host,hbl]])

        if res:
            st.success("You have the chance for getting placed...")
            send_mail_to_user(email,2)
        else:
            st.error("You may not get placed... Try to improve yourself")
            send_mail_to_user(email,3)
