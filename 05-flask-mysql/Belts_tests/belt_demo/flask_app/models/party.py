from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from datetime import datetime
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Party:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']  #! Must add to Create
        self.title = data_dict['title']
        self.location = data_dict['location']
        self.all_ages = data_dict['all_ages']
        self.date = data_dict['date']
        self.description = data_dict['description']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        # self.creator = ""


    # _________________________________CREATE
    
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO parties (user_id, title, location, all_ages, date, description) 
        VALUES (%(user_id)s, %(title)s, %(location)s, %(all_ages)s, %(date)s, %(description)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    # _________________________________GET ALL
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM parties
                    JOIN users on parties.user_id = users.id;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_parties =[]
        for row in results:
            party = cls(row)
            party.poster = f"{row['first_name']} {row['last_name']}"
            all_parties.append(party)
        return all_parties
    
    # ____________________________________GET USER PARTIES ********

    @classmethod
    def get_user_parties(cls, data_dict):
        query = """SELECT * FROM parties WHERE user_id = %(user_id)s"""
        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        all_parties =[]
        for row in results:
            all_parties.append(cls(row))
        return all_parties


    # _________________________________GET ONE

    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM parties
                    JOIN users ON parties.user_id = users.id
                    WHERE parties.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print(cls(result[0]))
        party = cls(result[0])
    
        party.creator = result[0]['first_name']
        return party
    
    # # _________________________________GET ONE

    # @classmethod
    # def get_by_id(cls, data_dict):
    #     query = """SELECT * FROM parties
    #                 JOIN users ON parties.user_id = users.id
    #                 WHERE parties.id=%(id)s;"""
    #     result = connectToMySQL(DATABASE).query_db(query, data_dict)
    #     print(cls(result[0]))
    #     party = cls(result[0])
    
    #     party.creator = result[0]['first_name']
    #     return party
    
    # _________________________________UPDATE 

    @classmethod
    def update(cls,data_dict):
        query= """UPDATE parties
                SET 
                title= %(title)s, location= %(location)s,
                all_ages= %(all_ages)s, date= %(date)s, 
                description= %(description)s
                WHERE id= %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    


    # ___________________________________DELETE
    
    @classmethod
    def delete(cls,data_dict):
        query= """DELETE FROM parties WHERE id= %(id)s; """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    

    # __________________________________VALIDATION
    @staticmethod
    def validate(data_dict):
        is_valid = True
        # date = datetime.strftime(data_dict["date"])
        # print("******************************",date,"******************************")
        if len(data_dict['title'])<2:
            is_valid =False
            flash("Title not valid", "title")

        if len(data_dict['location'])<2:
            is_valid =False
            flash("Location not valid", "location")

        if len(data_dict["description"])<7:
            is_valid = False
            flash("Description too short", "description")
        if data_dict["date"] =="":
            is_valid = False
            flash("Date too short", "date")
        # elif date < datetime.now().date:
        #     is_valid = False
        #     flash("Date Already passed", "date")
        return is_valid