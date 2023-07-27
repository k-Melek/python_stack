from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app) # we are creating an object called bcrypt, 

#! WORKING ON REGISTER !!

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", user = logged_user)

@app.route('/users/create', methods=['POST'])
def register():
    print('🎈'*10,request.form,'🎈'*10)
    if User.validate_register(request.form):

        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print("PASSWORD :",request.form['password'])
        print("Hashed PASSWORD :",pw_hash)
        data_dict = {
            **request.form,
            'password':pw_hash
        }
        user_id = User.create(data_dict) # CREATE USER & Take id in the return
        session['user_id'] = user_id

        return redirect('/dashboard')
    return redirect('/')

#! WORKING ON LOGIN !!
@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    user_from_db = User.get_by_email({'email':request.form['email']})
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            flash("Wrong Password !")
            print("You have an account", "login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/dashboard')
    flash("Wrong Email!", "login")
    return redirect('/')
    
@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect('/')
