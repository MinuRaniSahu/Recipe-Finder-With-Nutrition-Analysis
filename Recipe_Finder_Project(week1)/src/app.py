import streamlit as st
import requests

# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------

st.set_page_config(page_title="Global Recipe Finder", layout="wide")
st.title("🌎 Global Recipe Finder (Spoonacular Free API)")
st.write("Search recipes worldwide and get ingredients, preparation steps, and images!")

# Function to fetch recipe
def get_recipe(dish_name):
    # Step 1: Search for the recipe to get the Spoonacular ID
    search_url = "https://api.spoonacular.com/recipes/complexSearch"
    search_params = {"query": dish_name, "number": 1, "apiKey": API_KEY}
    
    try:
        search_response = requests.get(search_url, params=search_params, timeout=10)
        search_response.raise_for_status()
        search_data = search_response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Network/API error: {e}")
        return None

    if "results" not in search_data or len(search_data["results"]) == 0:
        return None

    recipe_id = search_data["results"][0]["id"]  # Spoonacular ID

    # Step 2: Get full recipe information
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    info_params = {"includeNutrition": False, "apiKey": API_KEY}

    try:
        info_response = requests.get(info_url, params=info_params, timeout=10)
        info_response.raise_for_status()
        recipe_data = info_response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Network/API error: {e}")
        return None

    # Ingredients
    ingredients = [ing["original"] for ing in recipe_data.get("extendedIngredients", [])]

    # Preparation steps
    steps = []
    instructions = recipe_data.get("analyzedInstructions", [])
    if instructions:
        steps = [step["step"] for step in instructions[0].get("steps", [])]

    return {
        "id": recipe_id,
        "title": recipe_data.get("title"),
        "image": recipe_data.get("image"),
        "ingredients": ingredients,
        "steps": steps
    }

# --------------------------
# Streamlit user interface
dish = st.text_input("Enter recipe name:")

if st.button("Search"):
    if not dish.strip():
        st.warning("Please enter a recipe name.")
    else:
        recipe = get_recipe(dish)
        if recipe:
            st.subheader(f"{recipe['title']} (Spoonacular ID: {recipe['id']})")
            
            if recipe["image"]:
                st.image(recipe["image"], width=400)
            
            st.markdown("**Ingredients:**")
            for ing in recipe["ingredients"]:
                st.write(f"- {ing}")
            
            st.markdown("**Preparation Steps:**")
            for i, step in enumerate(recipe["steps"], start=1):
                st.write(f"{i}. {step}")
        else:
            st.error("Recipe not found, please try another dish.")
