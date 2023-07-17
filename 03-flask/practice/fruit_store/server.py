from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry_quantity = request.form.get('strawberry')
    raspberry_quantity = request.form.get('raspberry')
    apple_quantity = request.form.get('apple')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    student_id = request.form.get('student_id')
    return render_template("checkout.html",strawberry_quantity=strawberry_quantity,
raspberry_quantity=raspberry_quantity,
apple_quantity=apple_quantity,
first_name=first_name,
last_name=last_name,
student_id=student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    