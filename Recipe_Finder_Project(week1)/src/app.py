import streamlit as st
from main1 import DevSearch_expedition

st.title("Recipe Finder")

dish = st.text_input("Enter recipe name")

if dish:
    recipe = DevSearch_expedition(dish)

    if recipe:
        st.subheader("Ingredients:")
        for item in recipe["ingredients"]:
            st.write("- " + item)

        st.subheader("Steps:")
        for step in recipe["steps"]:
            st.write("- " + step)
    else:
        st.write("Recipe not found.")
