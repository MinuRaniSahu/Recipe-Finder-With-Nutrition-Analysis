import requests

# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------

def find_recipe(dish_name):
    """
    Search a recipe using Spoonacular API and return ingredients, preparation steps, title, ID, and image.
    """
    # Step 1: Search for the recipe
    search_url = "https://api.spoonacular.com/recipes/complexSearch"
    search_params = {
        "query": dish_name,
        "number": 1,
        "apiKey": API_KEY
    }

    try:
        search_response = requests.get(search_url, params=search_params, timeout=10)
        search_response.raise_for_status()
        search_data = search_response.json()
    except requests.exceptions.RequestException as e:
        print("Network/API error during search:", e)
        return None

    if "results" not in search_data or len(search_data["results"]) == 0:
        print("Recipe not found.")
        return None

    recipe_id = search_data["results"][0]["id"]

    # Step 2: Get full recipe information
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    info_params = {
        "includeNutrition": False,
        "apiKey": API_KEY
    }

    try:
        info_response = requests.get(info_url, params=info_params, timeout=10)
        info_response.raise_for_status()
        recipe_data = info_response.json()
    except requests.exceptions.RequestException as e:
        print("Network/API error fetching recipe details:", e)
        return None

    # Extract ingredients
    ingredients = [ing["original"] for ing in recipe_data.get("extendedIngredients", [])]

    # Extract preparation steps
    steps = []
    instructions = recipe_data.get("analyzedInstructions", [])
    if instructions:
        steps = [step["step"] for step in instructions[0].get("steps", [])]

    # Get title and image
    title = recipe_data.get("title", "No Title")
    image = recipe_data.get("image", "")

    return {
        "id": recipe_id,
        "title": title,
        "image": image,
        "ingredients": ingredients,
        "steps": steps
    }

# --------------------------
# Main program
if __name__ == "__main__":
    print("🌎 Global Recipe Finder using Spoonacular API 🌎")
    while True:
        dish_name = input("\nEnter recipe name (or type 'exit' to quit): ").strip()
        if dish_name.lower() == "exit":
            print("Goodbye!")
            break
        if not dish_name:
            print("Please enter a valid recipe name.")
            continue

        recipe = find_recipe(dish_name)

        if recipe:
            print(f"\nTitle: {recipe['title']}")
            print(f"Recipe ID: {recipe['id']}")
            if recipe['image']:
                print(f"Image URL: {recipe['image']}")

            print("\nIngredients:")
            for ing in recipe['ingredients']:
                print("-", ing)

            print("\nPreparation Steps:")
            for i, step in enumerate(recipe['steps'], start=1):
                print(f"{i}. {step}")
        else:
            print("Recipe not found. Please try another dish.")
