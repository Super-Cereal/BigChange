from flask import Blueprint, redirect, abort, render_template
from flask_login import login_required, current_user

from data import db_session
from data.model_users import User

from .macros.delete_downloads_structure import delete_downloads_structure
from .macros.delete_file_if_exists import delete_file_if_exists
from .macros.save_file import save_file

from forms.form_edit_user import FormEditUser


blueprint = Blueprint('users', __name__,
                      template_folder='templates')


@blueprint.route('/users/', methods=['GET', 'POST'])
def users():
    session = db_session.create_session()
    users = session.query(User).all()
    return render_template('users.html', users=users)


@blueprint.route('/user/<int:user_id>')
def user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404)
    return render_template('user.html', user=user)


@blueprint.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if user_id != current_user.id:
        abort(403)
    form = FormEditUser()
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if form.validate_on_submit():
        user.name = form.name.data
        if form.photo.data:
            delete_file_if_exists(file=user.photo, session=session)
            user.photo = save_file(user, file=form.photo)
        session.commit()
        return redirect(f'/user/{user_id}')
    else:
        form.name.data = user.name
        return render_template('form_edit_user.html', form=form)


@blueprint.route('/del_user_photo/<int:user_id>', methods=['GET', 'POST'])
@login_required
def del_user_photo(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404)
    elif current_user.id != user.id:
        abort(403)
    delete_file_if_exists(file=user.photo, session=session)
    return redirect(f'/user/{user_id}')


@blueprint.route('/del_user/<int:user_id>')
@login_required
def del_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404)
    if current_user.id != user_id and current_user.type != 0:
        abort(403)
    delete_downloads_structure(user)
    session.delete(user)
    session.commit()
    return redirect('/')
