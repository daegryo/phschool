from flask import Flask, render_template
from flask import Flask, url_for, redirect, render_template
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.users import User
from forms.login import WelcomeForm
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    form = WelcomeForm()
    if form.validate_on_submit():
        return redirect('/login')


    return render_template('index.html', form=form)

@app.route('/login')
def login():
    form = WelcomeForm()
    return render_template('base.html', form=form)


if __name__ == '__main__':

    app.run(port=8080, host='127.0.0.1', debug=True)
