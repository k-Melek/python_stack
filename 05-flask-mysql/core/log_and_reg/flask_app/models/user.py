from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re	


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9.+_-]+$')

class User:

    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users 
                    (first_name, last_name, email, password)
                    VALUES 
                    (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id =%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False
    
    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if len(data_dict['first_name'])< 2:
            flash("First Name too short !", "first_name")
            is_valid = False
        if len(data_dict['last_name'])< 2:
            flash("Last Name too short !", "last_name")
            is_valid = False
        if len(data_dict['password'])< 7:
            flash("Password must contain at least 1 uppercase letter, 1 number, and be at least 8 characters long.", "password")
            is_valid = False
        if not PASSWORD_REGEX.match(data_dict['password']): 
            flash("Password must contain at least 1 uppercase letter, 1 number, and be at least 8 characters long.", "password")
            is_valid = False
        elif data_dict['password'] != data_dict['confirm_password']:
            flash("Password and Confirm Password Dont Match!", "confirm_password")
            is_valid = False
        if not EMAIL_REGEX.match(data_dict['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        elif User.get_by_email({'email':data_dict['email']}):
            flash("Email Already taken . Hope by you !", "email")
            is_valid = False
        return is_valid