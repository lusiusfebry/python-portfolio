import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)
with col1:
    st.image("images/test222.png")

with col2:
    st.title("Lusius Febrianus Maro")
    content = """
    Hi, I am Lusius Maro! I am a technical support specialist. I have over 10 years experience in field of Information 
    technology. On November 2022, i got laid off and now I currently learn python for career changer.
    This website as portfolio as a journal of learning python.
    """
    st.info(content)