from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.party import Party
from flask_app.models.user import User

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

#___________________________________________SHOW One


@app.route('/parties/<int:party_id>')

def one_party(party_id):
    if not 'user_id' in session:
        return redirect('/')
    one_party = Party.get_by_id({'id':party_id})
    return render_template("show_party.html", party = one_party)

#___________________________________________SHOW Many Parties

@app.route('/my_parties')

def my_parties():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_by_email({'id':session['user_id']})
    parties = Party.get_user_parties({'user_id':session['user_id']})
    return render_template("my_parties.html", user = user , parties = parties)


#___________________________________________UPDATE

@app.route('/parties/<int:party_id>/edit')
def edit_party(party_id):
    if not 'user_id' in session:
        return redirect('/')
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



@app.route('/parties/<int:party_id>/destroy', methods=['POST'])
def destroy(party_id):
    Party.delete({'id':party_id})
    return redirect('/dashboard')

