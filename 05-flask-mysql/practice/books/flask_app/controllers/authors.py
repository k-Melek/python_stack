

from flask import render_template, request, redirect, flash
from flask_app import app
from flask_app.models.author import Author
from flask_app.models import book, author

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors', methods=['GET'])
def show_authors():
    authors = author.Author.get_all_authors()
    return render_template('authors.html', authors=authors)

@app.route('/authors', methods=['POST'])
def create_author():
    name = request.form['name']
    new_author_id = author.Author.create(name)
    if new_author_id:
        flash('New author created successfully!', 'success')
    else:
        flash('Failed to create a new author.', 'danger')
    return redirect('/authors')

@app.route('/authors/<int:author_id>', methods=['GET'])
def show_author(author_id):
    author = Author.get_one_by_id(author_id)
    if not author:
        flash('Author not found.', 'danger')
        return redirect('/authors')
    favorite_books = author.get_favorite_books()
    all_books = book.Book.get_all_books()
    return render_template('show_author.html', author=author, favorite_books=favorite_books, all_books=all_books)

@app.route('/authors/<int:author_id>/add_favorite', methods=['POST'])
def add_favorite_book(author_id):
    book_id = request.form.get('book_id')
    if book_id:
        if author.Author.add_favorite_book(author_id, book_id):
            flash('Book added as a favorite!', 'success')
        else:
            flash('Failed to add the book as a favorite.', 'danger')
    return redirect(f'/authors/{author_id}')
