import requests
import logging

# ------------------- ADD YOUR API KEY -------------------
API_KEY = "YOUR_REAL_API_KEY_HERE"

# ------------------- LOGGING SETUP -------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def search_recipes(ingredients, diet):
    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
        "apiKey": API_KEY,
        "includeIngredients": ingredients,
        "number": 5,
        "addRecipeInformation": True
    }

    # Add diet filter properly
    if diet in ["vegetarian", "vegan"]:
        params["diet"] = diet

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if not data.get("results"):
            print("\nNo recipes found.")
            logging.warning("No recipes returned.")
            return

        print("\nRecipes Found:\n")

        for recipe in data["results"]:
            print("Recipe Name:", recipe["title"])
            print("Ready in:", recipe["readyInMinutes"], "minutes")
            print("Servings:", recipe["servings"])
            print("Image URL:", recipe["image"])
            print("-" * 40)

        logging.info("Recipes fetched successfully")

    except requests.exceptions.RequestException as e:
        print("Actual Error:", e)
        logging.error(f"API Error: {e}")

# ------------------- MAIN PROGRAM -------------------

print("🍽️ Recipe Finder Application – Week 2")

ingredients = input("Enter ingredients (comma separated): ")
diet = input("Enter diet (vegetarian / vegan / none): ").lower()

if diet == "none":
    diet = ""

search_recipes(ingredients, diet)