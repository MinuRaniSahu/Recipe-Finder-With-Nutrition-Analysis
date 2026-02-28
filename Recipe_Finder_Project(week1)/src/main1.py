def DevSearch_expedition(dish):
    recipes = {
        "egg curry": {
            "ingredients": [
                "Eggs",
                "Onion",
                "Tomato",
                "Chili powder",
                "Salt",
                "Oil"
            ],
            "steps": [
                "Boil the eggs",
                "Fry onion and tomato",
                "Add spices",
                "Add boiled eggs",
                "Cook for 10 minutes"
            ]
        },
        "omelette": {
            "ingredients": [
                "Eggs",
                "Salt",
                "Pepper",
                "Oil"
            ],
            "steps": [
                "Beat the eggs",
                "Add salt and pepper",
                "Pour into pan",
                "Cook both sides"
            ]
        }
    }

    dish = dish.lower()

    if dish in recipes:
        return recipes[dish]
    else:
        return None
