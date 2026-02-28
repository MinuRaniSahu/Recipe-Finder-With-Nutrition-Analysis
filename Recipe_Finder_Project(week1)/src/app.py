# app.py
import streamlit as st
from main1 import DevSearch_expedition

st.set_page_config(page_title="Recipe Finder", page_icon="🍲")
st.title("🍲 Recipe Finder App")
st.write("Search for any recipe and see ingredients and preparation steps.")

dish = st.text_input("Enter recipe name")

if st.button("Search"):
    if not dish.strip():
        st.info("Please type a recipe name to search.")
    else:
        recipe = DevSearch_expedition(dish)
        if recipe:
            st.success("Recipe Found Successfully! 🎉")
            st.subheader("Ingredients:")
            for ingredient in recipe["ingredients"]:
                st.write("-", ingredient)
            st.subheader("Preparation Steps:")
            for i, step in enumerate(recipe["steps"], 1):
                st.write(f"{i}. {step}")
        else:
            st.warning(f"No recipe found for '{dish}'.")

st.markdown("---")
st.write("Developed as part of Internship Project")
