import streamlit as st
import requests

st.set_page_config(page_title="Recipe Finder", layout="wide")
st.title("🍲 Recipe Finder")
st.write("Type the name of any recipe and get ingredients, preparation steps, and image.")

API_KEY = "77dec99f1d134a65899d295ef2386615"

def search_recipe(dish):
    # Search for up to 5 recipes
    search_url = "https://api.spoonacular.com/recipes/complexSearch"
    search_params = {
        "query": dish,
        "number": 5,   # fetch multiple results
        "apiKey": API_KEY
    }
    search_response = requests.get(search_url, params=search_params).json()

    if "results" not in search_response or len(search_response["results"]) == 0:
        return None

    recipes = []
    for r in search_response["results"]:
        recipe_id = r["id"]
        info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        info_response = requests.get(info_url, params={"includeNutrition": False, "apiKey": API_KEY}).json()

        ingredients = [ing["original"] for ing in info_response.get("extendedIngredients", [])]
        steps = []
        instructions = info_response.get("analyzedInstructions", [])
        if instructions:
            steps = [step["step"] for step in instructions[0].get("steps", [])]

        recipes.append({
            "title": info_response.get("title"),
            "image": info_response.get("image"),
            "ingredients": ingredients,
            "steps": steps
        })

    return recipes

# User input
recipe_name = st.text_input("Enter recipe name:")

if st.button("Search"):
    if not recipe_name.strip():
        st.warning("Please enter a recipe name.")
    else:
        recipes = search_recipe(recipe_name)
        if recipes:
            for recipe in recipes:
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
            st.error(f"No recipe found for '{recipe_name}'.")
