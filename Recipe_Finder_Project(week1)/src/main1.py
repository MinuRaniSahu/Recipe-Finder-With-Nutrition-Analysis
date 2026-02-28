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

        # Ingredients (fallback if extendedIngredients missing)
        ingredients = []
        for i in recipe.get("extendedIngredients", []):
            if "original" in i and i["original"]:
                ingredients.append(i["original"])
        if not ingredients:
            # Try alternate field if available
            if recipe.get("ingredients"):
                ingredients = recipe["ingredients"]

        # Preparation steps (safely handle missing analyzedInstructions)
        steps = []
        instructions = recipe.get("analyzedInstructions", [])
        if instructions and isinstance(instructions, list):
            steps_data = instructions[0].get("steps", [])
            for step in steps_data:
                if "step" in step and step["step"]:
                    steps.append(step["step"])

        # If nothing found, add a friendly message
        if not ingredients:
            ingredients = ["No ingredients found for this recipe."]
        if not steps:
            steps = ["No preparation steps found for this recipe."]

        return {"ingredients": ingredients, "steps": steps}

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)
    except Exception as e:
        print("Error fetching recipe:", e)

    return None
