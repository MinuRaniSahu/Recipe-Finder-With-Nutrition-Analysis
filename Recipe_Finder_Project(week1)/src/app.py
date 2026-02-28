import streamlit as st
from main1 import DevSearch_expedition

# Page configuration
st.set_page_config(page_title="Recipe Finder", page_icon="🍲")

# Stylish title
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🍲 Recipe Finder App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>Search for any recipe and see ingredients and preparation steps!</p>", unsafe_allow_html=True)
st.markdown("---")

# Input box
dish = st.text_input("🍽️ Enter recipe name here")

# Search button
if st.button("🔍 Search"):
    if not dish.strip():
        st.warning("Please type a recipe name to search!")
    else:
        recipe = DevSearch_expedition(dish)

        if recipe:
            st.success(f"✅ Recipe Found: **{dish.title()}**")

            # Ingredients section
            st.markdown("### 🧂 Ingredients")
            for ingredient in recipe["ingredients"]:
                st.markdown(f"- {ingredient}")

            # Preparation steps section
            st.markdown("### 👩‍🍳 Preparation Steps")
            for i, step in enumerate(recipe["steps"], 1):
                st.markdown(f"{i}. {step}")

        else:
            st.error(f"❌ Recipe not found for '{dish}'. Try another dish!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#888;'>Developed as part of Internship Project</p>", unsafe_allow_html=True)
