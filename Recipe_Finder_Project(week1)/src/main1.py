def DevSearch_expedition(dish):
    recipes = {
        "egg curry": {
            "ingredients": [
                "4 boiled eggs",
                "1 chopped onion",
                "2 chopped tomatoes",
                "1 tsp chili powder",
                "1/2 tsp turmeric",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "steps": [
                "Heat oil in a pan",
                "Add chopped onions and sauté until golden brown",
                "Add tomatoes and cook until soft",
                "Add spices and mix well",
                "Add boiled eggs and cook for 5-7 minutes",
                "Serve hot"
            ]
        },
        "omelette": {
            "ingredients": [
                "2 eggs",
                "Salt to taste",
                "Pepper",
                "1 tbsp oil"
            ],
            "steps": [
                "Beat the eggs in a bowl",
                "Add salt and pepper",
                "Heat oil in a pan",
                "Pour egg mixture",
                "Cook both sides until golden"
            ]
        },
        "veg pulao": {
            "ingredients": [
                "1 cup rice",
                "1/2 cup mixed vegetables",
                "1 chopped onion",
                "Spices",
                "2 cups water",
                "Salt to taste"
            ],
            "steps": [
                "Wash and soak rice",
                "Fry onions in oil",
                "Add vegetables and spices",
                "Add rice and water",
                "Cook until rice is soft"
            ]
        },
        "pasta": {
            "ingredients": [
                "1 cup pasta",
                "1/2 cup tomato sauce",
                "1 tbsp oil",
                "Salt",
                "Vegetables (optional)"
            ],
            "steps": [
                "Boil pasta until soft",
                "Heat oil in pan",
                "Add vegetables",
                "Add tomato sauce",
                "Mix pasta and cook for 2-3 minutes"
            ]
        }
    }

    dish = dish.lower()

    if dish in recipes:
        return recipes[dish]
    else:
        return None
