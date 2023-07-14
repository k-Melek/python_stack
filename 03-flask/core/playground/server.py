from flask import Flask, render_template
app=Flask(__name__)


@app.route('/play')
def play_level1():
    return render_template('index2.html', number=3, color="rgb(159,197,248)")

@app.route('/play/<int:numberIterance>/<colorOfBox>')
def play_level2_3(numberIterance, colorOfBox):
    return render_template('index2.html', number=numberIterance, color=colorOfBox)


if __name__ ==('__main__'):
    app.run(debug=True)