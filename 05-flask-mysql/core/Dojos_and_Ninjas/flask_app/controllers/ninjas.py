from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models import dojo


@app.route('/ninjas/add', methods=['GET'])
def add_ninja_form():
    dojos = dojo.Dojo.get_all()
    return render_template('add_ninja.html', dojos=dojos)    

@app.route('/ninjas', methods=['POST'])    
def add_ninja():
    data = {    
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    ninja_id = Ninja.add_ninja(data)
    return redirect(f'/dojos/{data["dojo_id"]}')    