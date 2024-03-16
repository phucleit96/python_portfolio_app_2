import streamlit as st

st.header("Contact Me")

with st.form(key='email_form'):
    
    st.image('fulllogo.png', width=350)
    user_email = st.text_input("Your Email Address", key='email')
    message = st.text_area("Your message", key='message')
    button = st.form_submit_button("Submit")
    if button:
        pass