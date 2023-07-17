
from flask import Flask, render_template , request, redirect, session
app = Flask(__name__)
app.secret_key = "No Secrets in GitHub"



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("*"*20, "PROCESS - FORM RECEIVED", "*"*20)
    # * Print on SERVER the object REQUEST 
    print("$"*20, request.form, "$"*20)
    print(f"USERNAME: {request.form['username']}\nAGE: {request.form['age']}\nFAVORITE FOOD: {request.form['favorite_food']}")

    session['username'] = request.form['username']
    session['age'] = request.form['age']
    session['favorite_food'] = request.form['favorite_food']

    # ! NEVER RENDER template in POST request 
    # return render_template('display.html', username = request.form['username'], age = request.form['age'], favorite_food = request.form['favorite_food'] ) 
    return redirect('/display')


@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')


@app.route('/display', methods=['GET'])
def display():
    print("✌"*20, request.form,"✌"*20)


    return render_template('display.html')



if __name__ == "__main__":
    app.run(debug=True, port=5003)
