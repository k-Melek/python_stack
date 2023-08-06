from flask import Flask

app = Flask(__name__)

app.secret_key = "recipes_demo"
DATABASE = "recipes_db"