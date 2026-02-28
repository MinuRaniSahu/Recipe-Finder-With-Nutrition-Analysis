import streamlit as st
from main1 import DevSearch_expedition

st.set_page_config(page_title="Recipe Finder", page_icon="🍲")
st.title("🍲 Recipe Finder App")
st.write("Search for any recipe and see ingredients and preparation steps.")

# Input box
dish = st.text_input("Enter recipe name")

# Button to trigger search
if st.button("Search"):
    if not dish.strip():
        st.warning("Please type a recipe name!")
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
            st.error("Recipe not found. Try another dish.")

# Footer
st.markdown("---")
st.write("Developed as part of Internship Project")
