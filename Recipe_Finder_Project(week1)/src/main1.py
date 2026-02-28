import requests

API_KEY = "77dec99f1d134a65899d295ef2386615" # Replace with your valid Spoonacular key

def DevSearch_expedition(dish):
    """
    Searches for a recipe by name using Spoonacular API
    Returns a dictionary with 'ingredients' and 'steps' if found, else None
    """
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": dish,
        "number": 1,
        "addRecipeInformation": True,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("results"):
            recipe = data["results"][0]

            ingredients = [
                ingredient["original"]
                for ingredient in recipe.get("extendedIngredients", [])
            ]

            steps = []
            instructions = recipe.get("analyzedInstructions", [])
            if instructions:
                steps = [step["step"] for step in instructions[0].get("steps", [])]

            return {"ingredients": ingredients, "steps": steps}

    except Exception as e:
        print("Error fetching recipe:", e)

    return None
