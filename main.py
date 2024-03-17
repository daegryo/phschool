from flask import Flask, render_template, request
from flask import Flask, url_for, redirect, render_template
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.users import User
from forms.login import LoginForm
from forms.uploads import UploadForm
from forms.registration import RegistrationForm
from werkzeug.utils import secure_filename
from os import remove

from flask_uploads import configure_uploads, IMAGES, UploadSet




app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOADED_IMAGES_DEST'] = 'static/uploads/images'
login_manager = LoginManager()
login_manager.init_app(app)

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        user.set_password(form.password.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            print('jjjjjjjj')
            return redirect(f"/home/<{form.email.data}>")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/login/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User()
        user.name = form.name.data
        print(form.name.data)
        user.about = form.about.data
        user.email = form.email.data
        user.set_password(str(form.password.data))
        user.hashed_password = user.password_hash
        db_sess.add(user)
        db_sess.commit()
        return redirect(f"/login")
    return render_template('registration.html', form=form)

@app.route('/home/<email>/personal-class', methods=['GET', 'POST'])
def personal_class(email):
    form = UploadForm()

    new_email = ''
    for el in email:
        if el != '<' and el != '>':
            print(el)
            new_email += el
    print(email, new_email)
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == new_email).first()
    print('v')
    if request.method == 'POST' and  form.validate_on_submit():
        print('lllllllll')
        filename = images.save(form.image.data)
        print(filename.split()[0])
        user.photo = filename.split()[0]
        db_sess.commit()
        return render_template('personal_class.html', user=user, form=form, image=user.photo)
    elif user.photo != '1':
        return render_template('personal_class.html', user=user, form=form, image=user.photo)


    return render_template('personal_class.html', user=user, form=form, image='')


@app.route('/home/<email>')
def home(email):
    new_email = ''
    for el in email:
        if el != '<' and el != '>':
            print(el)
            new_email += el
    print(new_email)

    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == new_email).first()
    print(type(user))
    return render_template('home.html', user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1', debug=True)
