import threading
import pandas as pd
import matplotlib.pyplot as plt
import time

# ------------------------------
# Sample Recipe Database (Demo Data)
# ------------------------------

recipes = {
    "Pasta": {
        "Calories": 400,
        "Protein": 12,
        "Carbs": 60,
        "Fat": 10
    },
    "Omelette": {
        "Calories": 250,
        "Protein": 18,
        "Carbs": 2,
        "Fat": 20
    },
    "Salad": {
        "Calories": 150,
        "Protein": 5,
        "Carbs": 20,
        "Fat": 5
    }
}

# ------------------------------
# Multithreading Function
# ------------------------------

def fetch_recipe(recipe_name):
    print("\nFetching recipe details...")
    time.sleep(2)  # Simulating API delay

    if recipe_name in recipes:
        nutrition = recipes[recipe_name]
        print("Recipe found successfully!\n")
        display_nutrition(recipe_name, nutrition)
    else:
        print("Recipe not found. Please try again.")

# ------------------------------
# Display using Pandas
# ------------------------------

def display_nutrition(recipe_name, nutrition):
    df = pd.DataFrame(nutrition.items(), columns=["Nutrient", "Value"])
    
    print("Nutritional Breakdown for", recipe_name)
    print(df)

    visualize_nutrition(recipe_name, nutrition)

# ------------------------------
# Matplotlib Visualization
# ------------------------------

def visualize_nutrition(recipe_name, nutrition):
    nutrients = list(nutrition.keys())
    values = list(nutrition.values())

    plt.figure()
    plt.bar(nutrients, values)
    plt.title(f"Nutritional Breakdown of {recipe_name}")
    plt.xlabel("Nutrients")
    plt.ylabel("Amount")
    plt.show()

# ------------------------------
# Improved UI
# ------------------------------

def main():
    print("=================================")
    print("     WEEK 3 - RECIPE FINDER     ")
    print("=================================")
    print("\nAvailable Recipes:")
    
    for recipe in recipes.keys():
        print("-", recipe)

    choice = input("\nEnter recipe name: ")

    # Multithreading implementation
    thread = threading.Thread(target=fetch_recipe, args=(choice,))
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()