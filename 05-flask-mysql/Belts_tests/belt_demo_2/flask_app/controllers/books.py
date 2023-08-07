from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.user import User

#___________________________________________CREATE

@app.route('/books/new')
def new_book():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("new_book.html")




@app.route('/books/create', methods=['POST'])
def add_book():
    print("***************************************************",request.form)
    if Book.validate(request.form):
        data= {
            **request.form,
            'user_id':session['user_id']
        }
        Book.create(data)
        return redirect('/books')
    return redirect('/books/new')

#___________________________________________SHOW One


@app.route('/books/<int:book_id>')

def one_book(book_id):
    if not 'user_id' in session:
        return redirect('/')
    one_book = Book.get_by_id({'id':book_id})
    return render_template("show_book.html", book = one_book)

#___________________________________________SHOW Many books

@app.route('/my_books')

def my_books():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_by_email({'id':session['user_id']})
    books = Book.get_user_books({'user_id':session['user_id']})
    return render_template("my_books.html", user = user , books = books)


#___________________________________________UPDATE

@app.route('/books/<int:book_id>/edit')
def edit_book(book_id):
    if not 'user_id' in session:
        return redirect('/')
    my_book = Book.get_by_id({'id':book_id})
    print("🎈"*20, my_book)
    return render_template("edit_book.html", book = my_book)

@app.route('/books/<int:book_id>/update', methods=['POST'])
def update_book(book_id):
    
    data = {
        **request.form,
        'id':book_id
    }
    Book.update(data)
    
    return redirect('/books')


#___________________________________________DELETE



@app.route('/books/<int:book_id>/destroy', methods=['POST'])
def destroy(book_id):
    Book.delete({'id':book_id})
    return redirect('/books')

