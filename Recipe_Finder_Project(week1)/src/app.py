import streamlit as st
import requests

API_KEY = "77dec99f1d134a65899d295ef2386615"  # Replace with your Spoonacular API key

def get_recipe_by_name(dish):
    """
    Search worldwide recipe on Spoonacular and return ingredients, steps, and recipe ID
    """
    search_url = "https://api.spoonacular.com/recipes/complexSearch?query=pasta&number=1&apiKey=YOUR_FREE_API_KEY"
    try:
        search_response = requests.get(search_url, params=search_params, timeout=10)
        search_response.raise_for_status()
        search_data = search_response.json()
    except requests.exceptions.RequestException as e:
        print("Network/API error:", e)
        return None
    
    if "results" not in search_data or len(search_data["results"]) == 0:
        return None
    
    recipe_id = search_data["results"][0]["id"]  # Spoonacular ID
    
    # Get full recipe details
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    info_params = {"includeNutrition": False, "apiKey": API_KEY}
    
    try:
        info_response = requests.get(info_url, params=info_params, timeout=10)
        info_response.raise_for_status()
        recipe_data = info_response.json()
    except requests.exceptions.RequestException as e:
        print("Network/API error:", e)
        return None
    
    ingredients = [ing["original"] for ing in recipe_data.get("extendedIngredients", [])]
    
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

# --- Usage ---
dish_name = input("Enter recipe name: ")
recipe = get_recipe_by_name(dish_name)

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
    print("Recipe not found!")
