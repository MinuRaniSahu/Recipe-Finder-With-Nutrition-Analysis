import requests

API_KEY = "PASTE_YOUR_KEY_HERE"

def DevSearch_expedition(dish):

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

        # 🔐 Safe check for results
        if "results" in data and len(data["results"]) > 0:

            recipe = data["results"][0]

            ingredients = [
                ingredient["original"]
                for ingredient in recipe.get("extendedIngredients", [])
            ]

            steps = []
            instructions = recipe.get("analyzedInstructions", [])

            if instructions:
                steps = [
                    step["step"]
                    for step in instructions[0].get("steps", [])
                ]

            return {
                "ingredients": ingredients,
                "steps": steps
            }

        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None
