from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  data = request.form
  print(data)
  return render_template("login.html", text="Testing", user="Zeuz")

@auth.route('/logout')
def logout():
  return "<p>logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sing_up():
  if request.method == 'POST' :
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
      flash('Email must be greater than 3 characters.', category='error')
    if len(firstName) < 2:
      flash('First Name must be greater than 2 characters', category='error')
    elif len(password1) < 5:
      flash('Password must be grater than 5 chraracters', category='error')
    elif password1 != password2:
      flash('Passwords dont match', category='error')
    else:
      flash('Account created', category='success')


  return render_template("sign_up.html")