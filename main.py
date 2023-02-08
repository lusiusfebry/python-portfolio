import streamlit as st
import pandas as pd

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

content_app = """
Below you can find some of the apps I have built in Python. Feel free to contact me

"""
st.write(content_app)

df = pd.read_csv("data.csv",sep=";")

col3,col4 = st.columns(2)
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])

