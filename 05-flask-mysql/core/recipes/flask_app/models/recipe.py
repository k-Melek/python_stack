from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from datetime import datetime
from flask_app.models.user import User


class Recipe:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']  #! Must add to Create
        self.name = data_dict['name']
        self.description = data_dict['description']
        self.instructions = data_dict['instructions']
        self.date = data_dict['date']
        self.under_30 = data_dict['under_30']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']



    # _________________________________CREATE
    
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO recipes (user_id, name, description, instructions, date, under_30) 
        VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    

        # _________________________________GET ONE + Who made it

    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM recipes
                    JOIN users ON recipes.user_id = users.id
                    WHERE recipes.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        recipe = cls(result[0])
        recipe.creator = result[0]['first_name']
        return recipe
    

    # _________________________________GET ALL
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM recipes
                    JOIN users on recipes.user_id = users.id;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes =[]
        for row in results:
            recipe = cls(row)
            recipe.poster = f"{row['first_name']} {row['last_name']}"
            all_recipes.append(recipe)
        return all_recipes
    

    # _________________________________UPDATE 

    @classmethod
    def update(cls,data_dict):
        query= """UPDATE recipes
                SET 
                name= %(name)s, description= %(description)s,
                instructions= %(instructions)s, date= %(date)s, 
                under_30= %(under_30)s
                WHERE id= %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    


    # ___________________________________DELETE
    
    @classmethod
    def delete(cls,data_dict):
        query= """DELETE FROM recipes WHERE id= %(id)s; """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    

    #_____________VALIDATE RECIPE_______

    @staticmethod
    def validate_recipe(data_dict):
        is_valid = True
        if len(data_dict['name'])<2:
            is_valid =False
            flash("Name too short", "name")
        
        if len(data_dict['description'])<2:
            is_valid =False
            flash("Description too short", "description")
        
        if len(data_dict['instructions'])<2:
            is_valid =False
            flash("Instructions too short", "instructions")

        if data_dict["date"] =="":
            is_valid = False
            flash("Date is Required", "date")

        return is_valid

        