from flask import Flask, request, redirect, render_template
from helpers import is_valid
import os, re

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
    error_condition=False
    
    username=request.form['username']
    password=request.form['password']
    verify_pwd=request.form['verify']
    email=request.form['email']

    if not username:
        username_error="You must provide a username"
        error_condition=True
    else:
        if not is_valid(username):
            username_error="Provide valid username of 3-20 characters (numbers and letters only)"
            error_condition=True

    if not password:
        pwd_error="You must provide a password"
        error_condition=True
    elif not is_valid(password):
        pwd_error="You must provide a valid password of 3-20 characters (numbers and letters only)"
        error_condition=True
    elif password != verify_pwd:
        verify_pwd_error="Passwords do not match"
        error_condition=True

    if email:
        #validate email
        match = re.match('[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}\Z', email)

        if not match or not len(match.group()) <= 20:
            email_error="Provide a valid email of fewer than 20 characters (single @, . and no spaces)"
            error_condition=True

    if error_condition==True:
        #Always clear password fields under any error conditions, for security.
        password=''
    else:
        return render_template('welcome.html', title='User Signup', username=username)

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