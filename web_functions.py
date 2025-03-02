import sqlite3
import os
def check_recipe(word):
    db = sqlite3.connect(".database/recipe.db")
    db.row_factory = sqlite3.Row
    data = db.execute("SELECT recipeName FROM Recipe WHERE recipeName = ?", (word,)).fetchone()
    return data is not None



def check_recipe_ID(word):
    db = sqlite3.connect(".database/recipe.db")
    db.row_factory = sqlite3.Row
    data = db.execute("SELECT recipeID FROM Recipe WHERE recipeID = ?", (word,)).fetchone()
    return data is not None


