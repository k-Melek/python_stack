from flask import Flask, render_template
app = Flask(__name__)

#Main route 8by8
@app.route('/')
def draw_board_8_by_8():
    return render_template('index.html',numberx=8, numbery=8)

# 2nd Route X by 8
@app.route('/<int:x>')
def draw_board_x_by_8(x):
    return render_template('index.html',numberx=x, numbery=8)


# 3rd Route  X by Y
@app.route('/<int:x>/<int:y>')
def draw_board_x_by_y(x, y):
    return render_template('index.html', numberx=x, numbery=y)

if __name__=="__main__":       
    app.run(debug=True) 

