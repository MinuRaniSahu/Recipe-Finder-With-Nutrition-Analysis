import streamlit as st

st.set_page_config(page_title="Recipe Finder", layout="wide")
st.title("🍲 Recipe Finder")
st.write("Search for a recipe by name. Recipes will appear here once added.")

# Empty list for recipes
recipes = [
    # No recipes included here
]

# Search box
search_name = st.text_input("Enter recipe name")

if st.button("Search"):
    found = [r for r in recipes if search_name.lower() in r["title"].lower()]
    if found:
        for r in found:
            st.markdown(f"### **_{r['title']}_**")
            if r.get("image"):
                st.image(r["image"], width=400)
            st.markdown("**Ingredients:**")
            for ing in r["ingredients"]:
                st.write(f"- {ing}")
            st.markdown("**Preparation Steps:**")
            for i, step in enumerate(r["steps"], 1):
                st.write(f"{i}. {step}")
            st.markdown("---")
    else:
        if search_name.strip():  # only show info if user typed something
            st.info(f"No recipe found for '{search_name}'.")
