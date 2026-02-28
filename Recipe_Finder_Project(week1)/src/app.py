import streamlit as st
import requests
# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------

st.set_page_config(page_title="Global Recipe Finder", layout="wide")
st.title("🌎 Global Recipe Finder (Free)")

st.write("Type any recipe keyword and see matching recipes with ingredients, preparation steps, and image.")

def search_recipes(keyword):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={keyword}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Network/API error: {e}")
        return []

    if not data["meals"]:
        return []

    results = []
    for meal in data["meals"]:
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

        results.append({
            "id": meal["idMeal"],
            "title": meal["strMeal"],
            "image": meal["strMealThumb"],
            "ingredients": ingredients,
            "steps": steps
        })

    return results

# Input from user
keyword = st.text_input("Enter recipe keyword:")

if st.button("Search"):
    if not keyword.strip():
        st.warning("Please enter a recipe keyword.")
    else:
        recipes = search_recipes(keyword)
        if recipes:
            for recipe in recipes:
                # Bold + Italic title
                st.markdown(f"### **_{recipe['title']}_** (ID: {recipe['id']})")
                
                # Image
                if recipe["image"]:
                    st.image(recipe["image"], width=400)
                
                # Ingredients
                st.markdown("**Ingredients:**")
                for ing in recipe["ingredients"]:
                    st.write(f"- {ing}")
                
                # Preparation Steps
                st.markdown("**Preparation Steps:**")
                for i, step in enumerate(recipe["steps"], 1):
                    st.write(f"{i}. {step}")

                # Separator between recipes
                st.markdown("---")
        else:
            st.error("No matching recipes found. Try a different keyword.")
