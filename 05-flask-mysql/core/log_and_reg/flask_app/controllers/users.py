from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    if "user_id" not in session:
        return redirect('/')
    
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("success.html", user = logged_user)

# _____________________________________________________________ CREATE =REGISTER

@app.route('/users/create', methods=['POST'])
def register():
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data_dict = {
            **request.form,
            'password':pw_hash
        }
        user_id = User.create(data_dict)
        session['user_id'] = user_id
        return redirect('/success')
    return redirect('/')

# _____________________________________________________________ LOGIN = LOG

@app.route('/login', methods =['POST'])
def login():
    user_from_db = User.get_by_email({'email':request.form['email']})
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            # if we get False after checking the password
            flash("Wrong email / Password","login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/success')
    flash("Wrong Email / Password!","login")
    return redirect('/')



# _____________________________________________________________ LOGOUT = DELETE SESSION

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')