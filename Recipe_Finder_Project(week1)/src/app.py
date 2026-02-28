import streamlit as st
import json
import os
# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------
st.set_page_config(page_title="Recipe Finder", layout="wide")
st.title("🍲 Recipe Finder")

st.write("Type the name of the recipe you want to find. All recipes are loaded from the local dataset.")

# Load recipes
recipes_file = "recipes.json"
if os.path.exists(recipes_file):
    with open(recipes_file, "r", encoding="utf-8") as f:
        recipes = json.load(f)
else:
    st.error("Recipes JSON file not found!")
    recipes = []

# Search function
def search_recipe(recipe_name):
    results = []
    for recipe in recipes:
        if recipe_name.lower() in recipe["title"].lower():
            results.append(recipe)
    return results

# User input
recipe_name = st.text_input("Enter recipe name:")

if st.button("Search"):
    if not recipe_name.strip():
        st.warning("Please enter a recipe name.")
    else:
        found_recipes = search_recipe(recipe_name)
        if found_recipes:
            for recipe in found_recipes:
                st.markdown(f"### **_{recipe['title']}_** (ID: {recipe['id']})")
                if recipe.get("image"):
                    st.image(recipe["image"], width=400)
                st.markdown("**Ingredients:**")
                for ing in recipe["ingredients"]:
                    st.write(f"- {ing}")
                st.markdown("**Preparation Steps:**")
                for i, step in enumerate(recipe["steps"], 1):
                    st.write(f"{i}. {step}")
                st.markdown("---")
        else:
            st.error(f"No recipes found for '{recipe_name}'.")
