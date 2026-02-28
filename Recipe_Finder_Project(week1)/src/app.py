import streamlit as st

st.set_page_config(page_title="Indian Recipe Finder", layout="wide")
st.title("🍛 Indian Recipe Finder")
st.write(
    "Search for any Indian recipe and see ingredients, preparation steps, and image. "
    "Recipes are not included yet. You can add recipes later to see results."
)

# Empty list for recipes
indian_recipes = [
    # No recipes included in the code
]

# Function to search recipes by name
def search_recipe(name):
    results = []
    for recipe in indian_recipes:
        if name.lower() in recipe["title"].lower():
            results.append(recipe)
    return results

# User input
recipe_name = st.text_input("Enter recipe name:")

if st.button("Search"):
    if not recipe_name.strip():
        st.warning("Please enter a recipe name.")
    else:
        found_recipes = search_recipe(recipe_name)
        if found_recipes:
            for recipe in found_recipes:
                st.markdown(f"### **_{recipe['title']}_**")
                if recipe.get("image"):
                    st.image(recipe["image"], width=400)
                st.markdown("**Ingredients:**")
                for ing in recipe["ingredients"]:
                    st.write(f"- {ing}")
                st.markdown("**Preparation Steps:**")
                for i, step in enumerate(recipe["steps"], 1):
                    st.write(f"{i}. {step}")
                st.markdown("---")
        else:
            st.info(
                f"No recipe found for '{recipe_name}'. "
                "Add recipes to the list to see results."
            )
