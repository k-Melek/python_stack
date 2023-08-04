

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import book

class Author:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls, name):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        data = {
            'name': name
        }
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        result = connectToMySQL(DATABASE).query_db(query)
        authors = [cls(row) for row in result]
        return authors

    @classmethod
    def get_one_by_id(cls, author_id):
        query = "SELECT * FROM authors WHERE id = %(author_id)s;"
        data = {
            'author_id': author_id
        }
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else None

    def get_favorite_books(self):
        query = """SELECT books.* FROM books
            JOIN favorites ON books.id = favorites.book_id
            WHERE favorites.author_id = %(author_id)s;"""
        data = {
            'author_id': self.id
        }
        result = connectToMySQL(DATABASE).query_db(query, data)
        return [book.Book(book_data) for book_data in result]

    @classmethod
    def add_favorite_book(cls, author_id, book_id):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        data = {
            'author_id': author_id,
            'book_id': book_id
        }
        return connectToMySQL(DATABASE).query_db(query, data)

