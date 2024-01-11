# from .db import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, URL

class LoginForm(FlaskForm):
   employee_number = StringField('Employee number', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   submit = SubmitField('Login')