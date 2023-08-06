from flask import Flask

app = Flask(__name__)
app.secret_key= "testing log_reg"
DATABASE = "logreg_test_db"