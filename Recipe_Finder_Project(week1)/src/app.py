import os
import sys
import streamlit as st

st.write("Current directory:", os.getcwd())
st.write("Files here:", os.listdir())
st.write("Python path:", sys.path)
