from flask import Flask ,render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "1234"


@app.route('/')
def index():
    if 'visit_count' not in session:
        session['visit_count'] = 1
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def count():
    session['visit_count'] = session['visit_count']+1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    # session['visit_count'] = 0
    return redirect('/')





if __name__ == ('__main__'):
    app.run(debug=True) 