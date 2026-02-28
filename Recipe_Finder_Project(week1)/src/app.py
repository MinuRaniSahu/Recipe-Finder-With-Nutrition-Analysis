import streamlit as st
import requests

API_KEY = "77dec99f1d134a65899d295ef2386615"# Replace with your Spoonacular free API key

def find_recipe(dish):
    """
    Search a recipe using Spoonacular API and return ingredients and preparation steps
    """
    # Step 1: Search recipe
    search_url = "https://api.spoonacular.com/recipes/complexSearch"
    search_params = {
        "query": dish,
        "number": 1,
        "apiKey": API_KEY
    }

    try:
        search_response = requests.get(search_url, params=search_params, timeout=10)
        search_response.raise_for_status()
        search_data = search_response.json()
    except requests.exceptions.RequestException as e:
        print("Error during search request:", e)
        return None

    if "results" not in search_data or len(search_data["results"]) == 0:
        print("Recipe not found.")
        return None

    recipe_id = search_data["results"][0]["id"]

    # Step 2: Get full recipe information
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    info_params = {
        "includeNutrition": False,
        "apiKey": API_KEY
    }

    try:
        info_response = requests.get(info_url, params=info_params, timeout=10)
        info_response.raise_for_status()
        recipe_data = info_response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching recipe information:", e)
        return None

    # Extract ingredients
    ingredients = [
        ing["original"] for ing in recipe_data.get("extendedIngredients", [])
    ]

    # Extract preparation steps
    steps = []
    instructions = recipe_data.get("analyzedInstructions", [])
    if instructions:
        steps = [step["step"] for step in instructions[0].get("steps", [])]

    return {
        "id": recipe_id,
        "title": recipe_data.get("title"),
        "ingredients": ingredients,
        "steps": steps
    }

# --- Example usage ---
if __name__ == "__main__":
    dish_name = input("Enter recipe name: ")
    recipe = find_recipe(dish_name)
    if recipe:
        print(f"\nRecipe ID: {recipe['id']}")
        print(f"Title: {recipe['title']}")
        print("\nIngredients:")
        for ing in recipe["ingredients"]:
            print("-", ing)
        print("\nPreparation Steps:")
        for i, step in enumerate(recipe["steps"], start=1):
            print(f"{i}. {step}")
    else:
        print("Recipe not found or error occurred.")
