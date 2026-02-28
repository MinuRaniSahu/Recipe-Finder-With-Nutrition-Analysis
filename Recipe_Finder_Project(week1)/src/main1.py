def DevSearch_expedition(dish):

    recipes = {
        "egg curry": {
            "ingredients": [
                "4 boiled eggs",
                "2 chopped onions",
                "2 chopped tomatoes",
                "1 tsp chili powder",
                "Salt",
                "Oil"
            ],
            "steps": [
                "Heat oil in a pan",
                "Fry onions until golden",
                "Add tomatoes and spices",
                "Add boiled eggs",
                "Cook for 10 minutes",
                "Serve hot"
            ]
        },

        "omelette": {
            "ingredients": [
                "2 eggs",
                "Salt",
                "Pepper",
                "1 tbsp oil"
            ],
            "steps": [
                "Beat eggs in a bowl",
                "Add salt and pepper",
                "Heat oil in a pan",
                "Pour egg mixture",
                "Cook both sides",
                "Serve hot"
            ]
        },

        "pasta": {
            "ingredients": [
                "1 cup pasta",
                "1/2 cup tomato sauce",
                "1 tsp garlic",
                "Salt",
                "Olive oil"
            ],
            "steps": [
                "Boil pasta until soft",
                "Heat oil and fry garlic",
                "Add tomato sauce",
                "Mix pasta with sauce",
                "Cook for 3 minutes",
                "Serve hot"
            ]
        },

        "veg pulao": {
            "ingredients": [
                "1 cup basmati rice",
                "Mixed vegetables",
                "1 chopped onion",
                "1 tsp garam masala",
                "Salt",
                "2 cups water"
            ],
            "steps": [
                "Wash and soak rice",
                "Fry onion in oil",
                "Add vegetables and spices",
                "Add rice and water",
                "Cook until rice is soft",
                "Serve hot"
            ]
        }
    }

    # 🔥 Important line (handles caps and spaces)
    dish = dish.lower().strip()

    return recipes.get(dish)
