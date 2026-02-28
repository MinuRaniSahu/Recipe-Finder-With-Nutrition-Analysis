def DevSearch_expedition(dish):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": dish,
        "number": 1,
        "addRecipeInformation": True,
        "apiKey": "bcd787be9ab94bf987d2f7e4e925ae7b"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        # Debug prints
        print("Searching for:", dish)
        print("API response:", data)

        if data.get("results"):
            recipe = data["results"][0]
            ingredients = [i["original"] for i in recipe.get("extendedIngredients", [])]
            steps = []
            instructions = recipe.get("analyzedInstructions", [])
            if instructions:
                steps = [step["step"] for step in instructions[0].get("steps", [])]
            return {"ingredients": ingredients, "steps": steps}

    except Exception as e:
        print("Error fetching recipe:", e)

    return None

