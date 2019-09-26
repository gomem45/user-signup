
from flask import Flask, render_template, request, redirect, url_for, flash

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = '1b674b1a191ab0504f6ebf96f38d4012'

class UserSignup(FlaskForm):
    username = TextField('Username', 
               validators=[DataRequired(), Length(min=3, max=20)])
    email = TextField('Email address', validators=[Email()])
    password = PasswordField('Password', 
               validators=[DataRequired(), Length(min=3, max=20 )])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    @app.route("/", methods=['GET', 'POST'])
    def index():
        form = UserSignup()

        if form.validate_on_submit():
            return redirect(url_for('welcome'))

            # print signup_form.errors
            #    if request.method == 'POST':
            #        username = request.form['username']
            #       email = request.form['email']
            #       password = request.form['password']
            #        confirm_password = request.form['confirm_password']
            #
            # print(username)
        return render_template('home.html', form=form)
    
    @app.route("/welcome", methods=['GET', 'POST'])
    def welcome():
        #username = request.form(username.data)
        return render_template('welcome.html')
     
if __name__ == "__main__":
    app.run(debug=True)