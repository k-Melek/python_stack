from flask import Flask

app= Flask(__name__)
app.secret_key = ('alo alo')
DATABASE = "books_schema"