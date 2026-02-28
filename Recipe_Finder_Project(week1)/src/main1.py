import requests

API_KEY = "77dec99f1d134a65899d295ef2386615"


def DevSearch_expedition(dish):

    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
        "query": dish,
        "number": 1,
        "addRecipeInformation": True,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["results"]:
        recipe = data["results"][0]

        ingredients = [
            ingredient["original"]
            for ingredient in recipe["extendedIngredients"]
        ]

        steps = []
        if recipe.get("analyzedInstructions"):
            instructions = recipe["analyzedInstructions"][0]["steps"]
            steps = [step["step"] for step in instructions]

        return {
            "ingredients": ingredients,
            "steps": steps
        }

    return None
