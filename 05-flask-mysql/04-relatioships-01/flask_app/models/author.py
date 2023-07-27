from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.book import Book

class Author:

    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.nationality = data_dict['nationality']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        # List of all author books
        self.my_books= []


    @classmethod
    def get_all(cls):
        query=""" SELECT * FROM authors;"""
        query_2=""" SELECT * FROM authors
                    JOIN books ON authors.id = books.author_id;"""
        all_authors = []
        results = connectToMySQL(DATABASE).query_db(query)
        # print("*"*10 ,results ,"*"*10)  # TESTING PRINT
        for row in results:
            author = cls(row)
            all_authors.append(author)
        return all_authors

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO authors (name, nationality) VALUES (%(name)s, %(nationality)s)"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return result

    @classmethod
    def get_one_by_id_with_books(cls, data_dict):
        query="""SELECT * FROM authors 
                    LEFT JOIN books ON authors.id = books.author_id 
                    WHERE authors.id = %(id)s;"""

        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        if results:
            this_author = cls(results[0])
            for row in results:
                book_data ={
                    'id':row['books.id'],
                    'author_id':row['author_id'],
                    'title':row['title'],
                    'pages':row['pages'],
                    'release_year':row['release_year'],
                    'created_at':row['books.created_at'],
                    'updated_at':row['books.updated_at']
                }

                book = Book(book_data)
                print("🎈"*10,row['books.id'],row['title'], row['pages'], row['release_year'], row['author_id'], row['books.created_at'], )
                this_author.my_books.append(book)
            print(this_author.my_books)
            return this_author
        print("This author doesnt have a book")
        return None