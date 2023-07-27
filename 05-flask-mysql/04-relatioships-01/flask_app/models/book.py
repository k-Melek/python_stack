from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Book:

    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.author_id = data_dict['author_id']
        self.title = data_dict['title']
        self.pages = data_dict['pages']
        self.release_year = data_dict['release_year']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):
        query=""" 
            SELECT * FROM books;"""
        all_books = []
        results = connectToMySQL(DATABASE).query_db(query)
        for row in results:
            book = cls(row)
            all_books.append(book)
        return all_books

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO books (author_id, title, pages, release_year) 
                            VALUES (%(author_id)s, %(title)s, %(pages)s, %(release_year)s)"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return result