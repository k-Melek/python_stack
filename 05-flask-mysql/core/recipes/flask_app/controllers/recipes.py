from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# CREATE **************************

@app.route('/recipes/new')
def new_recipe():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("new_recipe.html")




@app.route('/recipes/create', methods=['POST'])
def add_recipe():
    print(request.form)
    if Recipe.validate_recipe(request.form):
        data= {
            **request.form,
            'user_id':session['user_id']
        }
        Recipe.create(data)
        return redirect('/recipes')
    return redirect('/recipes/new')


# SHOW ONE *********************************


@app.route('/recipes/<int:recipe_id>')
def one_recipe(recipe_id):
    one_recipe = Recipe.get_by_id({'id':recipe_id})
    current_user = User.get_by_id({'id':session['user_id']})
    return render_template("show_recipe.html", recipe = one_recipe, user= current_user)



# UPDATE *********************************

@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    my_recipe = Recipe.get_by_id({'id':recipe_id})
    return render_template("edit_recipe.html", recipe = my_recipe)

@app.route('/recipes/update/<int:recipe_id>' , methods=['POST'])
def update_recipe(recipe_id):
    data = {
        **request.form,
        'id':recipe_id
    }
    Recipe.update(data)
    return redirect('/recipes')

# DELETE *********************************

@app.route('/recipes/destroy/<int:recipe_id>', methods= ['POST'])
def destroy(recipe_id):
    Recipe.delete({'id':recipe_id})
    return redirect('/recipes')



