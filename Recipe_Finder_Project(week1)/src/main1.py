import requests

# Replace with your Spoonacular API key
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
        response.raise_for_status()  # Will raise error if request failed
        data = response.json()

        # Debug: print API response
        print("Searching for:", dish)
        print("API response:", data)

        if data.get("results"):
            recipe = data["results"][0]

            ingredients = [
                i.get("original", "") for i in recipe.get("extendedIngredients", [])
            ]

            steps = []
            instructions = recipe.get("analyzedInstructions", [])
            if instructions:
                steps = [step.get("step", "") for step in instructions[0].get("steps", [])]

            return {"ingredients": ingredients, "steps": steps}

    except Exception as e:
        print("Error fetching recipe:", e)

    return None

