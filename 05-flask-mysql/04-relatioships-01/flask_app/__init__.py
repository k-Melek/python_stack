from flask import Flask
app = Flask(__name__)
app.secret_key = 'melek'
DATABASE = "books_schema"