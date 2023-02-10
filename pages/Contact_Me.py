import streamlit as st

st.header("Contact Me")

with st.form(key="form_contact_me"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Input your message here")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        message = message + user_email
        
