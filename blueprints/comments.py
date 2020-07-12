from flask import Blueprint, redirect, render_template, abort
from flask_login import login_required, current_user

from data import db_session
from data.model_comments import Comment

from .forms.forms_comments import FormAddComment, FormEditComment


blueprint = Blueprint('comments', __name__,
                      template_folder='templates')


@blueprint.route('/add_comment/<int:event_id>', methods=["GET", "POST"])
def add_comment(event_id):
    if not current_user.is_authenticated:
        return render_template('comments_sorry.html')
    session = db_session.create_session()
    form = FormAddComment()
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            event_id=event_id,
            user_id=current_user.id
        )
        session.add(comment)
        session.commit()
        return redirect(f'/event/{event_id}')
    else:
        return render_template('form_add_comment.html', form=form)


@blueprint.route('/edit_comment/<int:comment_id>', methods=["GET", "POST"])
@login_required
def edit_comment(comment_id):
    session = db_session.create_session()
    comment = session.query(Comment).get(comment_id)
    if current_user.id != comment.user_id:
        abort(403)
    form = FormEditComment()
    if form.validate_on_submit():
        comment.content = form.content.data
        session.commit()
        return redirect(f'/event/{comment.event_id}')
    else:
        form.content.data = comment.content
        return render_template('form_edit_comment.html', form=form)


@blueprint.route('/del_comment/<int:comment_id>')
@login_required
def del_comment(comment_id):
    session = db_session.create_session()
    comment = session.query(Comment).get(comment_id)
    if current_user.id != comment.user_id and current_user.id != comment.event_id:
        abort(403)
    event_id = comment.event_id
    session.delete(comment)
    session.commit()
    return redirect(f'/event/{event_id}')
