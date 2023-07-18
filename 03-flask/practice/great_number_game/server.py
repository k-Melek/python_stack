from flask import Flask ,render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "1234"


def initialize_game():
    session['random_number'] = random.randint(1, 100)
    session['message'] = ''

@app.route('/', methods=['GET'])
def home():
    if 'random_number' not in session:
        initialize_game()

    return render_template('index.html', message=session['message'])

@app.route('/', methods=['POST'])
def handle_guess():
    guess = int(request.form['guess'])
    random_number = session['random_number']
    message = ''

    if guess < random_number:
        message = 'Too low, try again!'
    elif guess > random_number:
        message = 'Too high, try again!'
    else:
        message = 'Congratulations! You guessed the correct number!'
        initialize_game()

    session['message'] = message

    return redirect('/')


if __name__ == ('__main__'):
    app.run(debug=True) 