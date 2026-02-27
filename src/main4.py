# Week 4 Final Project
# Recipe Finder with GUI

import tkinter as tk
from tkinter import messagebox

# Sample recipe data
recipes = {
    "Pasta": "Ingredients: Pasta, Tomato Sauce, Cheese\nSteps: Boil pasta. Add sauce. Mix cheese.",
    "Omelette": "Ingredients: Eggs, Salt, Pepper\nSteps: Beat eggs. Pour into pan. Cook well.",
    "Salad": "Ingredients: Lettuce, Tomato, Cucumber\nSteps: Chop vegetables. Mix and serve."
}

# Function to search recipe
def search_recipe():
    recipe_name = entry.get().strip()

    if recipe_name == "":
        messagebox.showwarning("Input Error", "Please enter a recipe name.")
        return

    if recipe_name in recipes:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, recipes[recipe_name])
    else:
        messagebox.showerror("Not Found", "Recipe not found!")

# Create window
root = tk.Tk()
root.title("Recipe Finder")
root.geometry("400x400")

# Label
label = tk.Label(root, text="Enter Recipe Name:")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Search button
search_button = tk.Button(root, text="Search", command=search_recipe)
search_button.pack(pady=10)

# Result text box
result_text = tk.Text(root, height=10, width=40)
result_text.pack(pady=10)

# Run app
root.mainloop()