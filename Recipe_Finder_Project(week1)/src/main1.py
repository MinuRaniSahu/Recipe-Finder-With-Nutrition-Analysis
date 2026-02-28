import requests

API_KEY = "d755e6b3393c47248c45774d7b254f3c"

def DevSearch_expedition(dish: str):
    """
    Search Spoonacular for a recipe and return ingredients and preparation steps
    """

    # Step 1: Search for the recipe
    search_url = "https://api.spoonacular.com/recipes/complexSearch"
    search_params = {
        "query": dish,
        "number": 1,
        "apiKey": API_KEY
    }

    try:
        search_resp = requests.get(search_url, params=search_params)
        search_resp.raise_for_status()
        search_data = search_resp.json()

        if not search_data.get("results"):
            return None  # Recipe not found

        recipe_id = search_data["results"][0]["id"]

        # Step 2: Fetch full recipe information by ID
        info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        info_params = {"apiKey": API_KEY}
        info_resp = requests.get(info_url, params=info_params)
        info_resp.raise_for_status()
        recipe = info_resp.json()

        # Ingredients
        ingredients = [i.get("original", "") for i in recipe.get("extendedIngredients", [])]

        # Steps
        steps = []
        instructions = recipe.get("analyzedInstructions", [])
        if instructions:
            steps = [step.get("step", "") for step in instructions[0].get("steps", [])]

        # Friendly message if empty
        if not ingredients:
            ingredients = ["No ingredients found."]
        if not steps:
            steps = ["No preparation steps found."]

        return {"ingredients": ingredients, "steps": steps}

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)
    except Exception as e:
        print("Error fetching recipe:", e)

    return None
