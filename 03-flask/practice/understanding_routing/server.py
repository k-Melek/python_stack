from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hi/<first_name>')
def hi_name(first_name):
    return f"Hi {first_name}"

@app.route('/repeat/<int:number>/<string:word>')
def repeat(number, word):
    return f"{word} "*number

@app.route('/<path:undefined_route>')
def handle_undefined_route(undefined_route):
    return "Sorry! No response. Try again."

if __name__ == ('__main__'):
    app.run(debug=True)