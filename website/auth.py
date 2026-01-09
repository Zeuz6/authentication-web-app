from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  return render_template("login.html", text="Testing", user="Zeuz")

@auth.route('/logout')
def logout():
  return "<p>logout</p>"

@auth.route('/sign_up')
def sing_up():
  return render_template("sign_up.html")