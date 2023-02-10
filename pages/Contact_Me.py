import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="form_contact_me"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Input your message here")
    # message = message + "\n" + user_email
#     message = f"""\
#     Subject : New email from {user_email}
#
#     From : {user_email}
#    {raw_message}
#
# """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(user_email,raw_message)
        st.info("Your email was sent successfully")

