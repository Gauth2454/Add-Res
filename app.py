from flask import Flask, render_template, redirect, request, url_for
import sqlite3
import web_functions
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
        if request.method == "POST":
            recipename = request.form["recipeName"]
            if web_functions.check_recipe(recipename) == True:
                db = sqlite3.connect(".database/recipe.db")
                db.row_factory = sqlite3.Row
                data = db.execute("SELECT * FROM Recipe WHERE recipeName LIKE ?", (recipename,)).fetchall()
                return render_template('home.html', recipe=data, search=recipename)
            else:
                return render_template('home.html',message="Recipe not found")
        return render_template("home.html")


app.config["UPLOAD_FOLDER"] = "static/images/"

@app.route('/addRecipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == "POST":
        recipename = request.form['recipeName']
        date = request.form['date']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        notes = request.form['notes']
        recipeID = request.form['recipeID']
        image_file = request.files["image"]
        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image_file.save(image_path)
        else:
            image_path = "static/images/default.jpg"

        if web_functions.check_recipe_ID(recipeID) == False:
            db = sqlite3.connect(".database/recipe.db")
            db.execute("INSERT INTO Recipe(recipeName, date, ingredients, instructions, notes, recipeID, image_url) VALUES (?, ?, ?, ?, ?, ?, ?)", (recipename, date, ingredients, instructions, notes, recipeID, image_path))
            db.commit()

            message = "Your recipe is added!"
            return render_template('addRecipe.html', confirm=message)
        else:
            return render_template('addRecipe.html', error="Recipe ID is already taken, Choose another one")

    return render_template('addRecipe.html')

app.config["UPLOAD_FOLDER"] = "static/images/"

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        recipename = request.form['recipeName']
        date = request.form['date']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        notes = request.form['notes']
        recipeID = request.form['recipeID']
        image_file = request.files["image"]
        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image_file.save(image_path)
            image_url=image_path
        else:
            image_url = "static/images/default.jpg"

        if web_functions.check_recipe_ID(recipeID) == True:
            db = sqlite3.connect(".database/recipe.db")
            db.execute("UPDATE Recipe SET recipeName=?, date=?, ingredients=?, instructions=?, notes=?, image_url=? WHERE recipeID=?", (recipename, date, ingredients, instructions, notes, image_url, recipeID))
            db.commit()

            message = "Your recipe is Updated!"
            return render_template('update.html', confirm=message)
        else:
            return render_template('update.html', error="Couldn't update the Recipe")

    return render_template('update.html')


@app.route('/catalogue')
def catalogue():
    db = sqlite3.connect(".database/recipe.db")
    db.row_factory = sqlite3.Row
    RecipeData = db.execute("SELECT * FROM Recipe").fetchall()
    return render_template('catalogue.html', recipe=RecipeData)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        recipeID = request.form['recipeID']

        if web_functions.check_recipe_ID(recipeID) == True:
            db = sqlite3.connect(".database/recipe.db")
            db.row_factory = sqlite3.Row
            db.execute("DELETE FROM Recipe WHERE RecipeID=?", (recipeID,))
            db.commit()
            return render_template('delete.html', message="Your Recipe is deleted")
        else:
            return render_template('delete.html',message="Recipe ID not found")
    return render_template("delete.html")

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

