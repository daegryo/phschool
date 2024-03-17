from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = StringField('О себе', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')