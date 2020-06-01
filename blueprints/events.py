from flask import Blueprint, redirect, render_template, abort, session as flask_session
from flask_login import login_required, current_user

from data import db_session
from data.model_events import Event

from .macros.delete_downloads_structure import delete_downloads_structure
from .macros.delete_file_if_exists import delete_file_if_exists
from .macros.save_file import save_file
from .macros.yandex_static_map import get_map

from .forms.forms_events import FormAddEvent, FormEditEvent


blueprint = Blueprint('events', __name__,
                      template_folder='templates')


@blueprint.route('/events_sorry')
def events_sorry():
    if current_user.is_authenticated:
        return render_template('events_reg_sorry.html')
    else:
        return render_template('events_unreg_sorry.html')


@blueprint.route('/events/', methods=['GET', 'POST'])
def events():
    session = db_session.create_session()
    events = session.query(Event).all()
    return render_template('events.html', events=events)


@blueprint.route('/event/<int:event_id>')
def event(event_id):
    session = db_session.create_session()
    event = session.query(Event).get(event_id)
    return render_template('event.html', event=event)


@blueprint.route('/add_event', methods=['GET', 'POST'])
def add_event():
    form = FormAddEvent()
    if not ((current_user.is_authenticated and flask_session.get('events_count', 0) < 10) or flask_session.get('events_count', 0) == 0):
        return redirect('/events_sorry')
    if form.validate_on_submit():
        session = db_session.create_session()
        event = Event(
            address=form.address.data,
            map_photo=get_map(form.address.data),
            content=form.content.data
        )
        session.add(event)
        session.commit()
        if form.photo.data:
            event.photo = save_file(event, form.photo)
            session.commit()
        flask_session['events_count'] = flask_session.get('events_count', 0) + 1
        return redirect(f'/event/{ event.id }')
    else:
        return render_template('form_add_event.html', form=form)


@blueprint.route('/edit_event/<event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    form = FormEditEvent()
    if form.validate_on_submit():
        session = db_session.create_session()
        event = session.query(Event).get(event_id)
        event.address = form.address.data
        event.map_photo = get_map(event.address)
        event.content = form.content.data
        if form.photo.data:
            delete_file_if_exists(event.photo)
            event.photo = save_file(event, form.photo)
        session.commit()
        return redirect(f'/event/{ event.id }')
    else:
        session = db_session.create_session()
        event = session.query(Event).get(event_id)
        form.address.data = event.address
        form.content.data = event.content
        return render_template('form_edit_event.html', form=form)


@blueprint.route('/del_event/<event_id>', methods=['GET', 'POST'])
@login_required
def del_event(event_id):
    session = db_session.create_session()
    event = session.query(Event).get(event_id)
    if not event:
        abort(404)
    elif current_user.id != event.user_id:
        abort(403)
    delete_downloads_structure(event)
    session.delete(event)
    session.commit()
    return redirect('/events')


@blueprint.route('/del_event_photo/<int:event_id>', methods=['GET', 'POST'])
@login_required
def del_event_photo(event_id):
    session = db_session.create_session()
    event = session.query(Event).get(event_id)
    if not event:
        abort(404)
    elif current_user.id != event.id:
        abort(403)
    delete_file_if_exists(file=event.photo, session=session)
    return redirect(f'/event/{event_id}')
