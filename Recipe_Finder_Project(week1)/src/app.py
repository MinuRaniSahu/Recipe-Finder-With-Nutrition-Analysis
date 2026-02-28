import streamlit as st

# Replace these with the actual function names in your code
from main1 import search_recipe
from main2 import get_nutrition
from main3 import something_week3
from main4 import something_week4

st.title("Recipe Finder with Nutrition Analysis")

recipe_input = st.text_input("Enter recipe name or ingredient:")

if st.button("Search"):
    result = search_recipe(recipe_input)
    nutrition = get_nutrition(result)
    extra = something_week3(result)
    final = something_week4(result)

    st.write(result)
    st.write(nutrition)
    st.write(extra)
    st.write(final)
