import streamlit as st
import requests
import json
import os
# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------
st.set_page_config(page_title="Indian & Global Recipe Finder", layout="wide")
st.title("🇮🇳 Indian & 🌍 Global Recipe Finder")

st.write("Type the name of the recipe you want to find. Choose Indian or Global.")

# Load Indian recipes from JSON
indian_file = "indian_recipes.json"
if os.path.exists(indian_file):
    with open(indian_file, "r", encoding="utf-8") as f:
        indian_recipes = json.load(f)
else:
    indian_recipes = []

# Search Indian recipes by exact or partial match
def search_indian(recipe_name):
    results = []
    for recipe in indian_recipes:
        if recipe_name.lower() in recipe["title"].lower():
            results.append(recipe)
    return results

# Search global recipes from TheMealDB by name
def search_global(recipe_name):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={recipe_name}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Network/API error: {e}")
        return []

    if not data["meals"]:
        return []

    results = []
    for meal in data["meals"]:
        ingredients = []
        for i in range(1, 21):
            ing = meal.get(f"strIngredient{i}")
            meas = meal.get(f"strMeasure{i}")
            if ing and ing.strip():
                ingredients.append(f"{meas.strip()} {ing.strip()}" if meas else ing.strip())
        steps = meal.get("strInstructions", "").split("\n")
        steps = [s.strip() for s in steps if s.strip()]
        results.append({
            "id": meal["idMeal"],
            "title": meal["strMeal"],
            "image": meal["strMealThumb"],
            "ingredients": ingredients,
            "steps": steps
        })
    return results

# Select recipe type
recipe_type = st.radio("Choose recipe type:", ["Indian", "Global"])
recipe_name = st.text_input("Enter the recipe name:")

if st.button("Search"):
    if not recipe_name.strip():
        st.warning("Please enter a recipe name.")
    else:
        if recipe_type == "Indian":
            recipes = search_indian(recipe_name)
            st.markdown("## 🇮🇳 Indian Recipes")
        else:
            recipes = search_global(recipe_name)
            st.markdown("## 🌍 Global Recipes")

        if recipes:
            for recipe in recipes:
                st.markdown(f"### **_{recipe['title']}_** (ID: {recipe.get('id', 'Local')})")
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
            st.error(f"No {recipe_type.lower()} recipes found for '{recipe_name}'.")
