import requests

API_KEY = "77dec99f1d134a65899d295ef2386615"

def DevSearch_expedition(dish):

  url = f"https://api.spoonacular.com/recipes/complexSearch?query={dish}&number=5&apiKey={77dec99f1d134a65899d295ef2386615}"
    params = {
        "query": dish,
        "number": 1,
        "addRecipeInformation": True,
        "apiKey": "77dec99f1d134a65899d295ef2386615"

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


