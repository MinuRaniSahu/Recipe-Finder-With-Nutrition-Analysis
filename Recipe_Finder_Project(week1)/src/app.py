import streamlit as st
from main1 import DevSearch_expedition

# Page Configuration
st.set_page_config(page_title="Recipe Finder", page_icon="🍲")

# Title
st.title("🍲 Recipe Finder App")
st.write("Find your favorite recipes instantly!")

# Input Box
dish = st.text_input("Enter recipe name")

# Search Logic
if dish:
    recipe = DevSearch_expedition(dish)

    if recipe:
        st.success("Recipe Found Successfully! 🎉")

        st.subheader("🧂 Ingredients:")
        for ingredient in recipe["ingredients"]:
            st.write("•", ingredient)

        st.subheader("👩‍🍳 Preparation Steps:")
        for step in recipe["steps"]:
            st.write("•", step)

    else:
        st.error("Recipe not found. Please try another dish.")

# Footer
st.markdown("---")
st.write("Developed as part of Internship Project")
