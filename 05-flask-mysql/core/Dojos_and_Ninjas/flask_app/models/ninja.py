from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



class Ninja:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.dojo_id = data_dict['dojo_id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.age = data_dict['age']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod
    def add_ninja(cls, data):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
                VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"""
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id    