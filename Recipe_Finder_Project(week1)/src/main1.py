import requests

API_KEY = "77dec99f1d134a65899d295ef2386615"

def DevSearch_expedition(dish):

    dish = dish.lower().strip()

    url = f"https://api.spoonacular.com/recipes/complexSearch?query={dish}&number=1&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if "results" in data and len(data["results"]) > 0:
        recipe = data["results"][0]

        return {
            "ingredients": ["Check full info requires premium plan"],
            "steps": ["Basic search result returned"]
        }

    return None
