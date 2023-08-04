from flask import render_template, request, redirect, flash
from flask_app import app
from flask_app.models import author
from flask_app.models.book import Book

@app.route('/books', methods=['GET'])
def show_books():
    books = Book.get_all_books()
    return render_template('books.html', books=books)

@app.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    num_of_pages = request.form['num_of_pages']
    new_book_id = Book.create(title, num_of_pages)
    if new_book_id:
        flash('New book created successfully!', 'success')
    else:
        flash('Failed to create a new book.', 'danger')
    return redirect('/books')

@app.route('/books/<int:book_id>', methods=['GET'])
def show_book(book_id):
    book = Book.get_one_by_id(book_id)
    if not book:
        flash('Book not found.', 'danger')
        return redirect('/books')
    favorite_authors = book.get_favorite_authors()
    all_authors = author.Author.get_all_authors()
    return render_template('show_book.html', book=book, favorite_authors=favorite_authors, all_authors=all_authors)

@app.route('/books/<int:book_id>/add_favorite', methods=['POST'])
def add_favorite_author(book_id):
    author_id = request.form.get('author_id')
    if author_id:
        if Book.add_favorite_author(book_id, author_id):
            flash('Author added as a favorite!', 'success')
        else:
            flash('Failed to add the author as a favorite.', 'danger')
    return redirect(f'/books/{book_id}')
