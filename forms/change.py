from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, FileField
from wtforms.validators import DataRequired
class ChangeForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = StringField('О себе', validators=[DataRequired()])

    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Внести изменения')
    image = FileField('image')