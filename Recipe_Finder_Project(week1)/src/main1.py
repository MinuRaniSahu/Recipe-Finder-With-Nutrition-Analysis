import requests

API_KEY = "d755e6b3393c47248c45774d7b254f3c"
def DevSearch_expedition(dish: str):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": dish,
        "number": 1,
        "addRecipeInformation": True,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        print("Searching for:", dish)  # Debug
        print("API response:", data)   # Debug

        results = data.get("results")
        if not results:
            return None

        recipe = results[0]

        # Safely get ingredients
        ingredients = [
            i.get("original", "") for i in recipe.get("extendedIngredients", [])
        ]

        # Safely get steps
        steps = []
        instructions = recipe.get("analyzedInstructions", [])
        if instructions and isinstance(instructions, list):
            steps = [step.get("step", "") for step in instructions[0].get("steps", [])]

        return {"ingredients": ingredients, "steps": steps}

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)
    except Exception as e:
        print("Error fetching recipe:", e)

    return None
