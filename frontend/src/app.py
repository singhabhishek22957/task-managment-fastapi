import streamlit as st 
from components.common.header import render_header
from components.common.sidebar import render_sidebar
st.set_page_config(
    page_title="Task Management",
    page_icon="✅",
    layout="wide"
)

user_role = "user"
user_name = "Abhishek"


# header 
render_header()

# sidebar 
render_sidebar()