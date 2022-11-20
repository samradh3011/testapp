import streamlit as st
from app import flaskapp

if not hasattr(st, 'already_started_server'):
    st.already_started_server = True
    flaskapp.run(port=8888)

st.text("It Worked")
