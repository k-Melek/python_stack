from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = all_dojos)

@app.route('/dojos', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_ninjas(id):
    dojos= Dojo.get_ninjas_by_dojo_id({'id':id})
    return render_template('show_ninjas.html', dojos = dojos)