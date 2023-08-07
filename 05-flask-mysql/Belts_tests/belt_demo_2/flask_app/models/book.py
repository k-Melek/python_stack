from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Book:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']  #! Must add to Create
        self.title = data_dict['title']
        self.author = data_dict['author']
        self.thoughts = data_dict['thoughts']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster = ""


    # _________________________________CREATE
    
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO books (user_id, title, author, thoughts) 
        VALUES (%(user_id)s, %(title)s, %(author)s, %(thoughts)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    # _________________________________GET ALL
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM books
                    JOIN users on books.user_id = users.id;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_books =[]
        for row in results:
            book = cls(row)
            book.poster = row['name']
            all_books.append(book)
        return all_books
    


    # _________________________________GET ONE

    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM books
                    JOIN users ON books.user_id = users.id
                    WHERE books.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print(cls(result[0]))
        book = cls(result[0])
    
        book.poster = result[0]['name']
        return book
    
    
    # _________________________________UPDATE 

    @classmethod
    def update(cls,data_dict):
        query= """UPDATE books
                SET 
                title= %(title)s, author= %(author)s,
                thoughts= %(thoughts)s
                WHERE id= %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    


    # ___________________________________DELETE
    
    @classmethod
    def delete(cls,data_dict):
        query= """DELETE FROM books WHERE id= %(id)s; """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    

    # __________________________________VALIDATION
    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['title'])<2:
            is_valid =False
            flash("Title not valid", "title")
        if len(data_dict['author'])<2:
            is_valid =False
            flash("Author not valid", "author")
        if len(data_dict["thoughts"])<7:
            is_valid =False
            flash("Thoughts too short", "thoughts")
        return is_valid