from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app import DATABASE


class Dojo:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.ninjas =[]


    @classmethod
    def create(cls, data_dict):
        query ="""INSERT INTO dojos (name)
                VALUES (%(name)s)"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos =[]
        for row in results:
            dojo= cls(row)
            all_dojos.append(dojo)
        return all_dojos
    
    @classmethod
    def get_ninjas_by_dojo_id(cls, data_dict):
        query = """SELECT * FROM dojos
                    left join ninjas on ninjas.dojo_id=dojos.id WHERE dojo_id= %(id)s"""
        
        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        print(results)
        dojo = cls(results[0])
        for i in results:
            ninja_dict= {
                'id' : i['ninjas.id'],
                'dojo_id' : i['dojo_id'],
                'first_name' : i['first_name'],
                'last_name' : i['last_name'],
                'age' : i['age'],
                'created_at' : i['ninjas.created_at'],
                'updated_at' : i['ninjas.updated_at']
            }
            ninja = Ninja(ninja_dict)
            dojo.ninjas.append(ninja)
        return dojo
