import streamlit as st
from main1 import DevSearch_expedition

st.title("🍲 Recipe Finder App")

# Input box
dish = st.text_input("🍽️ Enter recipe name here")

# Search button
if st.button("🔍 Search"):
    if not dish.strip():
        st.warning("Please type a recipe name!")
    else:
        recipe = DevSearch_expedition(dish)

        if recipe:
            st.success(f"✅ Recipe Found: {dish.title()}")

            st.subheader("🧂 Ingredients")
            for ing in recipe["ingredients"]:
                st.write("-", ing)

            st.subheader("👩‍🍳 Preparation Steps")
            for i, step in enumerate(recipe["steps"], 1):
                st.write(f"{i}. {step}")
        else:
            st.error(f"❌ Recipe not found for '{dish}'")
