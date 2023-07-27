from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all())

@app.route('/user/new')
def new():
    return render_template('create_user.html')

@app.route('/user/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        'id': id
    }
    return render_template('show_user.html', user= User.get_one(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit_user.html', user= User.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    print("*"*20, request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/')
