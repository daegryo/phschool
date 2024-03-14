from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class WelcomeForm(FlaskForm):
    submit = SubmitField('Log In')