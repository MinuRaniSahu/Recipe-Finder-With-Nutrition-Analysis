# Recipe Finder Application

recipes = {
    "pasta": { "ingredients": ["pasta", "salt", "water", "sauce"],
        "instructions": "Boil pasta. Add sauce. Mix well and serve." },
    "omelette": {"ingredients": ["egg", "salt", "oil"],
        "instructions": "Beat eggs. Heat oil. Cook eggs and serve." },
    "salad": { "ingredients": ["tomato", "cucumber", "salt", "lemon"],
        "instructions": "Chop vegetables. Mix everything and serve." }
}

def find_recipe(dish_name):
    dish_name = dish_name.lower()
    
    if dish_name in recipes:
        print("\nRecipe Found!")
        print("Ingredients:", ", ".join(recipes[dish_name]["ingredients"]))
        print("Instructions:", recipes[dish_name]["instructions"])
    else:
        print("\nSorry, recipe not found.")

def DevSearch_expedition(dish):
    return f"Recipe found for {dish}"
def DevSearch_expedition(dish):
    recipes = {
        "egg curry": {
            "ingredients": ["2 eggs", "1 onion", "2 tomatoes", "Spices"],
            "instructions": "Boil eggs. Prepare gravy. Add eggs and cook."
        },
        "pasta": {
            "ingredients": ["Pasta", "Tomato sauce", "Cheese"],
            "instructions": "Boil pasta. Add sauce. Mix well."
        }
    }

    dish = dish.lower()

    if dish in recipes:
        return recipes[dish]
    else:
        return "Recipe not found"


