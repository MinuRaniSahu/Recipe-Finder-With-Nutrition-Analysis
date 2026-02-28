import streamlit as st
import requests
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------

st.set_page_config(page_title="Global Recipe Finder", layout="wide")
st.title("🌎 Global Recipe Finder (Free)")

st.write("Type any recipe name and get ingredients, preparation steps, and image.")

def get_recipe(dish_name):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={dish_name}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Network/API error: {e}")
        return None

    if not data["meals"]:
        return None

    meal = data["meals"][0]

    # Ingredients
    ingredients = []
    for i in range(1, 21):
        ing = meal.get(f"strIngredient{i}")
        meas = meal.get(f"strMeasure{i}")
        if ing and ing.strip():
            ingredients.append(f"{meas.strip()} {ing.strip()}" if meas else ing.strip())

    # Preparation steps
    steps = meal.get("strInstructions", "").split("\n")
    steps = [s.strip() for s in steps if s.strip()]

    return {
        "id": meal["idMeal"],
        "title": meal["strMeal"],
        "image": meal["strMealThumb"],
        "ingredients": ingredients,
        "steps": steps
    }

dish = st.text_input("Enter recipe name:")

if st.button("Search"):
    if not dish.strip():
        st.warning("Please enter a recipe name.")
    else:
        recipe = get_recipe(dish)
        if recipe:
            st.subheader(f"{recipe['title']} (ID: {recipe['id']})")
            if recipe["image"]:
                st.image(recipe["image"], width=400)

            st.markdown("**Ingredients:**")
            for ing in recipe["ingredients"]:
                st.write(f"- {ing}")

            st.markdown("**Preparation Steps:**")
            for i, step in enumerate(recipe["steps"], 1):
                st.write(f"{i}. {step}")
        else:
            st.error("Recipe not found. Please try another dish.")
