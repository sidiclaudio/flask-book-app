from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegistrationForm(FlaskForm):
    name = StringField('Whats your name')
    email = StringField('Enter your E-mail')
    submit = SubmitField('Register')
