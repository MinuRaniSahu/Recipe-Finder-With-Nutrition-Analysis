import json

# --- Load recipes from JSON ---
with open("recipes.json", "r") as f:
    recipes = json.load(f)


# --- Search function ---
def search_recipe(dish):
    dish_lower = dish.strip().lower()
    for name, data in recipes.items():
        if name.lower() == dish_lower:
            return data
    # If recipe not found, return None
    return None


# --- App start ---
while True:
    dish = input("Enter recipe name: ").strip()
    recipe = search_recipe(dish)

    if recipe:
        print("\nIngredients:")
        for ing in recipe["ingredients"]:
            print("-", ing)
        print("\nSteps:")
        for i, step in enumerate(recipe["steps"], start=1):
            print(f"{i}. {step}")
    else:
        # This is where your existing error message goes
        print("Error: Recipe not found, please try another dish")

    cont = input("\nSearch another recipe? (y/n): ").strip().lower()
    if cont != "y":
        break
