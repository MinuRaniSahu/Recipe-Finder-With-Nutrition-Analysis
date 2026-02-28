import streamlit as st
import requests

# --- Your Spoonacular API key ---
API_KEY = "77dec99f1d134a65899d295ef2386615" # Replace with your real API key

# --- Function to search recipe globally ---
def find_recipe_global(dish):
    search_url = "https://api.spoonacular.com/recipes/complexSearch"
    search_params = {"query": dish, "number": 1, "apiKey": API_KEY}

    try:
        search_response = requests.get(search_url, params=search_params, timeout=10)
        search_response.raise_for_status()
        search_data = search_response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Network/API error: {e}")
        return None

    if "results" not in search_data or len(search_data["results"]) == 0:
        return None

    recipe_id = search_data["results"][0]["id"]

    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    info_params = {"includeNutrition": False, "apiKey": API_KEY}

    try:
        info_response = requests.get(info_url, params=info_params, timeout=10)
        info_response.raise_for_status()
        recipe_data = info_response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Network/API error: {e}")
        return None

    ingredients = [ing["original"] for ing in recipe_data.get("extendedIngredients", [])]

    steps = []
    instructions = recipe_data.get("analyzedInstructions", [])
    if instructions:
        steps = [step["step"] for step in instructions[0].get("steps", [])]

    return {"ingredients": ingredients, "steps": steps}


# --- Streamlit UI ---
st.title("🌎 Global Recipe Finder")
st.write("Search for any recipe from around the world and get its ingredients and preparation steps!")

dish = st.text_input("Enter recipe name:")

if st.button("Search"):
    if not dish.strip():
        st.warning("Please enter a recipe name.")
    else:
        recipe = find_recipe_global(dish)
        if recipe:
            st.subheader("Ingredients:")
            for ing in recipe["ingredients"]:
                st.write(f"- {ing}")

            st.subheader("Preparation Steps:")
            for i, step in enumerate(recipe["steps"], start=1):
                st.write(f"{i}. {step}")
        else:
            st.error("Recipe not found, please try another dish.")
