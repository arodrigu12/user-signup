from flask import Flask, request, redirect, render_template
from helpers import is_valid
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():

    return render_template('index.html', title='User Signup')

@app.route("/", methods=["POST"])
def validate_signup():

    username_error=''
    pwd_error=''
    verify_pwd_error=''
    email_error=''
    
    username=request.form['username']
    password=request.form['password']
    verify_pwd=request.form['verify']
    email=request.form['email']

    if not username:
        username_error="You must provide a username"
    else:
        if not is_valid(username):
            username_error="Provide valid username of 3-20 characters (numbers and letters only)"

    return render_template('index.html',
        title='User Signup',
        username=username,
        email=email,
        password=password,
        username_error=username_error,
        pwd_error=pwd_error,
        verify_pwd_error=verify_pwd_error,
        email_error=email_error)

app.run()