# Recipe Finder Application

recipes = {
    "pasta": { "ingredients": ["pasta", "salt", "water", "sauce"],
        "instructions": "Boil pasta. Add sauce. Mix well and serve." },
    "omelette": {"ingredients": ["egg", "salt", "oil"],
        "instructions": "Beat eggs. Heat oil. Cook eggs and serve." },
    "salad": {
        "ingredients": ["tomato", "cucumber", "salt", "lemon"],
        "instructions": "Chop vegetables. Mix everything and serve."
    }
}

def find_recipe(dish_name):
    dish_name = dish_name.lower()
    
    if dish_name in recipes:
        print("\nRecipe Found!")
        print("Ingredients:", ", ".join(recipes[dish_name]["ingredients"]))
        print("Instructions:", recipes[dish_name]["instructions"])
    else:
        print("\nSorry, recipe not found.")

def main():
    print("=== Welcome to Recipe Finder ===")
    dish = input("Enter recipe name: ")
    find_recipe(dish)

if __name__ == "__main__":

    main()

