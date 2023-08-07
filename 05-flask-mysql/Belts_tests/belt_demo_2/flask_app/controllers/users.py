from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.book import Book
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



#_____________________________________________ INDEX

@app.route('/')
def index():
    return render_template("index.html")

#__________________________________________ DASHBOARD

@app.route('/books')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    
    logged_user = User.get_by_id({'id':session['user_id']})
    books = Book.get_all()
    return render_template("dashboard.html", user = logged_user, books = books )

#___________________________________________ REGISTER

@app.route('/users/create', methods=['POST'])
def register():
    # Get The FORM ata from the fontend
    print(request.form)
    #VALIDATE the form  DATA
        #- if data is valid 
    if User.validate(request.form):

        # 1 Secure password = Hash using bcrypt
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password':pw_hash
        }

        # 2 Create the new user
        user_id = User.create(data) # return from create to follow USER
        session['user_id'] = user_id
        return redirect('/books')
    #- If data not valid
    return redirect('/')

# _____________________________________________ LOGIN

@app.route('/login', methods =['POST'])
def login():
    # 1 Get user by Email !
    user = User.get_by_email({'email':request.form['email']})
    # - If user DONT exist : error and message  > redirect 
    if not user:
        flash("Invalid Email / Password", "login")
        return redirect('/')
    # - If user exist : check password 
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email / Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/books')


#_____________________________________________ LOGOUT
@app.route('/logout', methods =['POST'])
def logout():
    session.clear()
    return redirect('/')
    