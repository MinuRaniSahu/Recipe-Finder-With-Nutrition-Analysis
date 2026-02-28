import streamlit as st
from main1 import DevSearch_expedition

# Page config
st.set_page_config(page_title="Recipe Finder", page_icon="🍲")

# Title
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🍲 Recipe Finder App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>Find ingredients and preparation steps instantly!</p>", unsafe_allow_html=True)
st.markdown("---")

# Input
dish = st.text_input("🍽️ Enter recipe name here")

# Search Button
if st.button("🔍 Search"):
    if not dish.strip():
        st.warning("Please type a recipe name!")
    else:
        recipe = DevSearch_expedition(dish)

        if recipe:
            st.success(f"✅ Recipe Found: **{dish.title()}**")
            
            # Ingredients
            st.markdown("### 🧂 Ingredients")
            for ingredient in recipe["ingredients"]:
                st.markdown(f"- {ingredient}")

            # Preparation Steps
            st.markdown("### 👩‍🍳 Preparation Steps")
            for i, step in enumerate(recipe["steps"], 1):
                st.markdown(f"{i}. {step}")

        else:
            st.error("❌ Recipe not found. Try another dish!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#888;'>Developed as part of Internship Project</p>", unsafe
