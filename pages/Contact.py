import streamlit as st
from send_email import send_email
import re


def validate_message_and_email(message, user_email):
    if not message:
        st.info("Message can't be blank")
        return False

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.match(email_regex, user_email):
        st.info("Invalid email address, example: a@gmail.com")
        return False

    return True


st.header("Contact Me")

with st.form(key='email_form'):
    st.image('fulllogo.png', width=350)
    user_subject = st.text_input("Email Subject", key='subject')
    user_email = st.text_input("Your Email Address", key='email')
    message = st.text_area("Your message", key='message')
    button = st.form_submit_button("Submit")

    if button:
        if validate_message_and_email(message, user_email):
            final_message = f"Subject: {user_subject} from {user_email}\n{message}\n{user_email}"
            send_email(message=final_message)
            st.info(f"Successfully sent! We will keep in touch! Have a great day {user_email}!!!")


