# app.py
import streamlit as st
from main1 import function_week1
from main2 import function_week2
from main3 import function_week3
from main4 import function_week4

st.title("Recipe Finder with Nutrition Analysis")

recipe_input = st.text_input("Enter recipe name or ingredient:")

if st.button("Search"):
    result = function_week1(recipe_input)
    nutrition = function_week2(result)
    extra_info = function_week3(result)
    final_output = function_week4(result)
    
    st.write(result)
    st.write(nutrition)
    st.write(extra_info)
    st.write(final_output)