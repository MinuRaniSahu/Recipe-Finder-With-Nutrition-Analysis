import streamlit as st
import requests
import json
import os
# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------
st.set_page_config(page_title="Global & Indian Recipe Finder", layout="wide")
st.title("🌎 Global & Indian Recipe Finder (Alternative Approach)")

st.write("Search recipes worldwide. Indian recipes come from local dataset, global recipes from TheMealDB.")

# Load Indian recipes dataset (you can expand this JSON)
indian_file = "indian_recipes.json"
if os.path.exists(indian_file):
    with open(indian_file, "r", encoding="utf-8") as f:
        indian_recipes = json.load(f)
else:
    indian_recipes = []

def search_indian(keyword):
    """Search Indian recipes in local dataset"""
    results = []
    for recipe in indian_recipes:
        if keyword.lower() in recipe["title"].lower():
            r = recipe.copy()
            r["is_indian"] = True
            results.append(r)
    return results

def search_global(keyword):
    """Search TheMealDB for global recipes"""
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
        indian_matches = search_indian(keyword)
        global_matches = search_global(keyword)
        all_recipes = indian_matches + global_matches

        if all_recipes:
            for recipe in all_recipes:
                title_md = f"### **_{recipe['title']}_** (ID: {recipe.get('id', 'Local')})"
                if recipe.get("is_indian"):
                    title_md = f"<span style='color:red'>{title_md}</span>"
                    st.markdown(title_md, unsafe_allow_html=True)
                else:
                    st.markdown(title_md)

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
            st.error("No recipes found. Try another keyword.")
