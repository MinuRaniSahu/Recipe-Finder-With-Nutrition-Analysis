import requests

# 🔑 Put your valid Spoonacular API key here
API_KEY = "bcd787be9ab94bf987d2f7e4e925ae7b"
def DevSearch_expedition(dish: str):
    """
    Searches for a recipe by name using Spoonacular API
    Returns a dictionary with 'ingredients' and 'steps' if found, else None
    """

    # Spoonacular API endpoint
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": dish,
        "number": 1,  # get only 1 recipe
        "addRecipeInformation": True,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise error if status != 200
        data = response.json()

        # 🔹 Debug: print what API returns
        print("Searching for:", dish)
        print("API response:", data)

        # Check if results exist
        if data.get("results"):
            recipe = data["results"][0]

            # Extract ingredients
            ingredients = [
                i.get("original", "") for i in recipe.get("extendedIngredients", [])
            ]

            # Extract preparation steps
            steps = []
            instructions = recipe.get("analyzedInstructions", [])
            if instructions:
                steps = [step.get("step", "") for step in instructions[0].get("steps", [])]

            return {"ingredients": ingredients, "steps": steps}

    except requests.exceptions.RequestException as

