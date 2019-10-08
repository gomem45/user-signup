
from flask import Flask, request, redirect, render_template, url_for 
import cgi 
import re   

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
   return render_template('index.html', title="Sign Up")


@app.route('/signup', methods=['POST', 'GET'])
def signup():

   username_error = ''
   password_error= '' 
   verify_error = '' 
   email_error = ''
    
   errors = []

   if request.method == 'POST':
      username = cgi.escape(request.form['username'])

      if username == '':
         username_error = 'Username field cannot be empty'
      
      elif len(username) <= 3 or len(username) > 20:
         username_error = 'Username must be between 3 and 20 characters'
         username = ''
      
      elif " " in username:
         username_error = 'Username cannot contain any spaces'
         username = ''
      
      errors.append(username_error)

      password = cgi.escape(request.form['password'])

      if password == '':
         password_error = 'Password field cannot be empty'
      
      elif len(password) <= 3 or len(password) > 20:
         username_error ='Password must be between 3 and 20 characters'
         password = ''
      
      errors.append(password_error)

      verify = cgi.escape(request.form['verify'])

      if password != verify:
         verify_error = 'Passwords do not match. Try again'

      errors.append(verify_error)

      email = cgi.escape(request.form['email'])


      if email != '':
         if len(email) <= 3 or len(email) > 20:
            email_error = 'Email must be between 3 and 20 characters'
            email = ''
         
         #elif not re.match(r"(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]-\.[a-zA-Z0-9-,.]+$)", email):
         elif "@" not in email or "." not in email:
            email_error = 'Email address is not valid'
            
      errors.append(email_error)

      if errors:
         return render_template('index.html', username = username,
            username_error = username_error, 
            password_error = password_error,
            verify_error = verify_error,
            email = email, 
            email_error = email_error)
      else:
         return render_template('welcome.html', username=username)
      
   return render_template('index.html')


if __name__ == '__main__':
   app.run()



         
         