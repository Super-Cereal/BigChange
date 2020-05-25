from flask import Blueprint, redirect, render_template
from flask_login import login_required, logout_user, login_user, LoginManager

from data import db_session
from data.model_users import User

from .forms.forms_users import FormAddUser, FormLogin

from .macros.save_file import save_file


blueprint = Blueprint('user_authenticate', __name__,
                      template_folder='templates')
login_manager = LoginManager()


@login_manager.user_loader
def user_load(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    form = FormAddUser()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            type=1
        )
        user.set_password(form.password.data)
        session = db_session.create_session()
        session.add(user)
        session.commit()
        if form.photo.data:
            user.photo = save_file(user, file=form.photo)
            session.commit()
        login_user(user, remember=form.remember.data)
        return redirect(f'/user/{user.id}')
    else:
        return render_template('form_add_user.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if not user or not user.check_password(form.password.data):
            return render_template('form_login.html', form=form, message="Invalid username or password")
        login_user(user, remember=form.remember.data)
        return redirect(f'/user/{user.id}')
    return render_template('form_login.html', form=form)


@blueprint.route('/logout/', methods=['GET', 'POST'])
@blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')
