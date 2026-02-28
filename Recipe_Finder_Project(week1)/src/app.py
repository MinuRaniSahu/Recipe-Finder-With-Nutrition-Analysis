import streamlit as st
from main1 import DevSearch_expedition

st.title("Recipe Finder")

dish = st.text_input("Enter recipe name")

if dish:
    result = DevSearch_expedition(dish)
    st.write(result)
