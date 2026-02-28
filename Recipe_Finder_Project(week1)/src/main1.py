import requests

# 🔑 Replace this with your real Spoonacular API key
API_KEY = "77dec99f1d134a65899d295ef2386615"

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

        # 🔹 Debug: print API response to terminal
        print("Searching for:", dish)
        print("API response:", data)

        # Check if the API returned any results
        if data.get("results"):
            recipe = data["results"][0]

            # Extract ingredients
            ingredients = [
                ingredient["original"]
                for ingredient in recipe.get("extendedIngredients", [])
            ]

            # Extract preparation steps
            steps = []
            instructions = recipe.get("analyzedInstructions", [])
            if instructions:
                steps = [step["step"] for step in instructions[0].get("steps", [])]

            return {"ingredients": ingredients, "steps": steps}

    except Exception as e:
        print("Error fetching recipe:", e)

    # Return None if recipe not found or API failed
    return None
