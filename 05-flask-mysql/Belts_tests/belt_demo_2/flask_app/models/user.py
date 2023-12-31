from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users (name, email, password) VALUES (%(name)s, %(email)s, %(password)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    

    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email=%(email)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result :
            return cls(result[0])
        return False
    
    
    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['name'])<2:
            is_valid =False
            flash("Name not valid", "name")
        if not EMAIL_REGEX.match(data_dict['email']): 
            is_valid = False
            flash("Email not valid", "email")
        # if data_dict email exist in the the database 
        elif User.get_by_email({'email': data_dict['email']}):
            is_valid = False
            flash("email already taken ","email")
        if len(data_dict["password"])<7:
            is_valid = False
            flash("Password too short", "password")
        elif data_dict["password"]!= data_dict["confirm_password"]:
            is_valid = False
            flash("Password and confirm password must match", "password")
        return is_valid