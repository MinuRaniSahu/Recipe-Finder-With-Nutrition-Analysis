import streamlit as st
from main1 import search_recipe
from main2 import get_nutrition
from main3 import week3_function
from main4 import week4_function

st.title("Recipe Finder with Nutrition Analysis")

recipe_input = st.text_input("Enter recipe name or ingredient:")

if recipe_input:
    try:
        st.write(search_recipe(recipe_input))
        st.write(get_nutrition(recipe_input))
        st.write(week3_function(recipe_input))
        st.write(week4_function(recipe_input))
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter a recipe name or ingredient")
