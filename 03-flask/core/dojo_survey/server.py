from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "khedher Melek"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["your_name"] = request.form["your_name"]
    session["dojo_location"] = request.form["dojo_location"]
    session["fav_language"] = request.form["fav_language"]
    session["message"] = request.form["message"]
    session["gender"] = request.form["gender"]
    session["more"] = request.form["more"]
    session["less"] = request.form["less"]
    return redirect("result")


@app.route("/result", methods=["GET"])
def display():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
