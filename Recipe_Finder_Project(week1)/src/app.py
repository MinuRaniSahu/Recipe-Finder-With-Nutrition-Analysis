import streamlit as st
import requests
import json
import os
# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------

st.set_page_config(page_title="Indian & Global Recipe Finder", layout="wide")
st.title("🌎 Indian & Global Recipe Finder")

st.write("Search recipes worldwide. Indian recipes are loaded from local JSON, global recipes from TheMealDB API. Results are shown in separate sections.")

# Load Indian recipes from local JSON
indian_file = "indian_recipes.json"
if os.path.exists(indian_file):
    with open(indian_file, "r", encoding="utf-8") as f:
        indian_recipes = json.load(f)
else:
    indian_recipes = []

# Function to search Indian recipes
def search_indian(keyword):
    results = []
    for recipe in indian_recipes:
        # Search in title and ingredients
        title_match = keyword.lower() in recipe["title"].lower()
        ingredient_match = any(keyword.lower() in ing.lower() for ing in recipe["ingredients"])
        if title_match or ingredient_match:
            r = recipe.copy()
            r["is_indian"] = True
            results.append(r)
    return results

# Function to search global recipes
def search_global(keyword):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={keyword}"
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
            "ingredients": ingredients,
            "steps": steps,
            "image": meal["strMealThumb"],
            "is_indian": False
        })
    return results

# User input
keyword = st.text_input("Enter recipe keyword:")

if st.button("Search"):
    if not keyword.strip():
        st.warning("Please enter a recipe keyword.")
    else:
        # Separate search
        indian_results = search_indian(keyword)
        global_results = search_global(keyword)

        # Indian Recipes Section
        st.markdown("## 🇮🇳 Indian Recipes")
        if indian_results:
            for recipe in indian_results:
                st.markdown(f"### **_{recipe['title']}_**")
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
            st.write("No Indian recipes found for this keyword.")

        # Global Recipes Section
        st.markdown("## 🌍 Global Recipes")
        if global_results:
            for recipe in global_results:
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
            st.write("No global recipes found for this keyword.")
