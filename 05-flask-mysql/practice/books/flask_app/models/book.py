
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import author


class Book:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.title = data_dict['title']
        self.num_of_pages = data_dict['num_of_pages']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls, title, num_of_pages):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        data = {
            'title': title,
            'num_of_pages': num_of_pages
        }
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        result = connectToMySQL(DATABASE).query_db(query)
        books = [cls(row) for row in result]
        return books

    @classmethod
    def get_one_by_id(cls, book_id):
        query = "SELECT * FROM books WHERE id = %(book_id)s;"
        data = {
            'book_id': book_id
        }
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else None

    def get_favorite_authors(self):
        query = """
            SELECT authors.* FROM authors
            JOIN favorites ON authors.id = favorites.author_id
            WHERE favorites.book_id = %(book_id)s;
        """
        data = {
            'book_id': self.id
        }
        result = connectToMySQL(DATABASE).query_db(query, data)
        return [author.Author(author_data) for author_data in result]

    @classmethod
    def add_favorite_author(cls, book_id, author_id):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);"
        data = {
            'book_id': book_id,
            'author_id': author_id
        }
        return connectToMySQL(DATABASE).query_db(query, data)
