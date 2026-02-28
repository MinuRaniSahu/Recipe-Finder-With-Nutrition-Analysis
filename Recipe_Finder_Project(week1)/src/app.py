import streamlit as st
# --------------------------
# Enter your Spoonacular free API key here
API_KEY = "77dec99f1d134a65899d295ef2386615"
# --------------------------
st.set_page_config(page_title="Recipe Finder", layout="wide")
st.title("🍲 Recipe Finder")
st.write(
    "You can add recipes below, then search for any recipe by name. "
    "No recipes are included in the code."
)

# Empty list for storing recipes
recipes = []

# Section to add a new recipe
st.header("Add a Recipe")
with st.form("add_recipe_form"):
    title = st.text_input("Recipe Title")
    ingredients_text = st.text_area(
        "Ingredients (one per line)"
    )
    steps_text = st.text_area(
        "Preparation Steps (one per line)"
    )
    image_url = st.text_input("Image URL (optional)")
    submit = st.form_submit_button("Add Recipe")

if submit:
    if not title.strip():
        st.warning("Please enter a recipe title.")
    else:
        recipe = {
            "title": title.strip(),
            "ingredients": [i.strip() for i in ingredients_text.split("\n") if i.strip()],
            "steps": [s.strip() for s in steps_text.split("\n") if s.strip()],
            "image": image_url.strip() if image_url.strip() else None,
        }
        recipes.append(recipe)
        st.success(f"Recipe '{title}' added successfully!")

# Section to search recipes
st.header("Search Recipes")
search_name = st.text_input("Enter recipe name to search:")

if st.button("Search"):
    if not search_name.strip():
        st.warning("Please enter a recipe name to search.")
    else:
        found = [r for r in recipes if search_name.lower() in r["title"].lower()]
        if found:
            for r in found:
                st.markdown(f"### **_{r['title']}_**")
                if r.get("image"):
                    st.image(r["image"], width=400)
                st.markdown("**Ingredients:**")
                for ing in r["ingredients"]:
                    st.write(f"- {ing}")
                st.markdown("**Preparation Steps:**")
                for i, step in enumerate(r["steps"], 1):
                    st.write(f"{i}. {step}")
                st.markdown("---")
        else:
            st.info(f"No recipe found for '{search_name}'.")
