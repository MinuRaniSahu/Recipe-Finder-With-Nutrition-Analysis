import requests

API_KEY = "77dec99f1d134a65899d295ef2386615"
def DevSearch_expedition(dish):

    # STEP 1: Search recipe
    search_url = "https://api.spoonacular.com/recipes/complexSearch"

    search_params = {
        "query": dish,
        "number": 1,
        "apiKey": API_KEY
    }

    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    if "results" not in search_data or len(search_data["results"]) == 0:
        return None

    recipe_id = search_data["results"][0]["id"]

    # STEP 2: Get full information
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"

    info_params = {
        "includeNutrition": False,
        "apiKey": API_KEY
    }

    info_response = requests.get(info_url, params=info_params)
    recipe_data = info_response.json()

    # Extract ingredients
    ingredients = [
        ing["original"]
        for ing in recipe_data.get("extendedIngredients", [])
    ]

    # Extract preparation steps
    steps = []
    instructions = recipe_data.get("analyzedInstructions", [])
    if instructions:
        steps = [
            step["step"]
            for step in instructions[0].get("steps", [])
        ]

    return {
        "ingredients": ingredients,
        "steps": steps
    }

