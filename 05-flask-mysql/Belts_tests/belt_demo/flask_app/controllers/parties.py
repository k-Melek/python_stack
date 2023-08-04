from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.party import Party

#___________________________________________CREATE

@app.route('/parties/new')
def new_party():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("new_party.html")




@app.route('/parties/create', methods=['POST'])
def add_party():
    print(request.form)
    if Party.validate(request.form):
        data= {
            **request.form,
            'user_id':session['user_id']
        }
        Party.create(data)
        return redirect('/dashboard')
    return redirect('/parties/new')

#___________________________________________SHOW


@app.route('/parties/<int:party_id>')
def one_party(party_id):
    one_party = Party.get_by_id({'id':party_id})
    return render_template("show_party.html", party = one_party)

#___________________________________________UPDATE

@app.route('/parties/<int:party_id>/edit')
def edit_party(party_id):
    my_party = Party.get_by_id({'id':party_id})
    print("🎈"*20, my_party)
    return render_template("edit_party.html", party = my_party)

@app.route('/parties/<int:party_id>/update', methods=['POST'])
def update_party(party_id):
    
    data = {
        **request.form,
        'id':party_id
    }
    Party.update(data)
    
    return redirect('/dashboard')


#___________________________________________DELETE



@app.route('/parties/<int:party_id>/destroy')
def destroy(party_id):
    Party.delete({'id':party_id})
    return redirect('/dashboard')

