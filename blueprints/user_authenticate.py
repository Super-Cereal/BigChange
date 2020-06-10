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


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form_registration = FormAddUser()
    form_login = FormLogin()
    if form_registration.validate_on_submit():
        user = User(
            name=form_registration.name_reg.data,
            email=form_registration.email_reg.data,
            type=1
        )
        user.set_password(form_registration.password_reg.data)
        session = db_session.create_session()
        session.add(user)
        session.commit()
        login_user(user, remember=form_registration.remember_reg.data)
        return redirect(f'/user/{user.id}')
    if form_login.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form_login.email_log.data).first()
        if not user or not user.check_password(form_login.password_log.data):
            return render_template('form_login.html', form_log=form_login, form_reg=form_registration, message_l="Invalid username or password")
        login_user(user, remember=form_login.remember_log.data)
        return redirect(f'/user/{user.id}')
    return render_template('form_login.html', form_log=form_login, form_reg=form_registration)


@blueprint.route('/logout/', methods=['GET', 'POST'])
@blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')
