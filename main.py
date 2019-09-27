from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


    

@app.route("/")
def index():
    
    return render_template('index.html')



@app.route('/validation', methods=['POST'])
def form_errors():
    name = request.form['username']
    passWord = request.form['pass']
    verification = request.form['verify']
    user_email = request.form['email']
    user_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if name == "":
    
        user_error = "This field cannot be empty"
    elif " " in name:
        user_error = "This field cannot contain spaces"
    elif len(name) < 3 or len(name) > 20:

        user_error = "User name must be between 3 and 20 characters"

        

        
    
    
        
        
    if passWord == "":
        password_error = "This field cannot be empty"
    elif " " in passWord:
        password_error = "This field cannot contain spaces"
    elif len(passWord) < 3 or len(passWord) > 20:
        password_error = "User name must be between 3 and 20 characters"
    
    if verification == "":
        verify_error = "This field cannot be empty"
    elif " " in verification:
        verify_error = "This field cannot contain spaces"
    elif verification != passWord:
        verify_error = "Passwords do not match"

    if user_email:

        char1 = "@"
        char2 = "."
        if char1 not in user_email or char2 not in user_email:
            email_error = "Email must contain @ and (.)"

        
    
    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', name=name)
        

    else:
        
        return render_template('index.html', user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
    

    
        

    


    

app.run()

