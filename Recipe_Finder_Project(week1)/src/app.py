import streamlit as st
import requests

API_KEY = "77dec99f1d134a65899d295ef2386615"  # Replace with your Spoonacular API key

def find_recipe_spoonacular(dish):
    # Step 1: Search recipe
    search_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {"query": dish, "number": 1, "apiKey": API_KEY}
    
    response = requests.get(search_url, params=params)
    data = response.json()
    
    if not data["results"]:
        return None
    
    recipe_id = data["results"][0]["id"]  # Spoonacular ID
    
    # Step 2: Get full recipe info
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    info_params = {"includeNutrition": False, "apiKey": API_KEY}
    
    info_response = requests.get(info_url, params=info_params)
    recipe_data = info_response.json()
    
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

# Example usage
dish_name = input("Enter recipe name: ")
recipe = find_recipe_spoonacular(dish_name)
if recipe:
    print(f"Recipe ID: {recipe['id']}")
    print("Ingredients:")
    for ing in recipe["ingredients"]:
        print("-", ing)
    print("\nPreparation Steps:")
    for i, step in enumerate(recipe["steps"], start=1):
        print(f"{i}. {step}")
else:
    print("Recipe not found!")
