from flask import Blueprint, redirect, render_template, abort
from flask_login import login_required, current_user

from data import db_session
from data.model_events import Event

from .macros.delete_downloads_structure import delete_downloads_structure
from .macros.save_file import save_file
from .macros.yandex_static_map import get_ll, get_map

from .forms.forms_events import FormAddEvent, FormAddEventAddition


blueprint = Blueprint('events', __name__,
                      template_folder='templates')


@blueprint.route('/events_sorry')
def events_sorry():
    return render_template('events_sorry.html')


@blueprint.route('/events/', methods=['GET', 'POST'])
def events():
    session = db_session.create_session()
    events = session.query(Event).all()
    return render_template('events.html', events=events)


@blueprint.route('/event/<int:event_id>')
def event(event_id):
    session = db_session.create_session()
    event = session.query(Event).get(event_id)
    map_photo = get_map(event.ll)
    return render_template('eventD.html', event=event, map_photo=map_photo)


@blueprint.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if not current_user.is_authenticated:
        return redirect('/events_sorry')
    form = FormAddEvent()
    if form.validate_on_submit():
        ll = get_ll(form.address.data)
        if not ll:
            return render_template('form_add_event.html', form=form, message="Addres not found")
        session = db_session.create_session()
        event = Event(
            address=form.address.data,
            ll=ll,
            content=form.content.data,
            user_id=current_user.id
        )
        session.add(event)
        session.commit()
        if form.photo.data:
            event.photo = save_file(event, form.photo)
            session.commit()
        return redirect(f'/event/{ event.id }')
    else:
        return render_template('form_add_event.html', form=form)


@blueprint.route('/add_event_addition/<int:event_id>', methods=['GET', 'POST'])
@login_required
def add_event_addition(event_id):
    session = db_session.create_session()
    event = session.query(Event).get(event_id)
    if current_user.id != event.user_id:
        abort(403)
    form = FormAddEventAddition()
    if form.validate_on_submit():
        if event.additions:
            event.additions = f'{event.additions}${form.content.data}'
        else:
            event.additions = form.content.data
        session.commit()
        return redirect(f'/event/{event_id}')
    else:
        return render_template('form_add_event_addition.html', form=form, event=event)


@blueprint.route('/del_event_addition/<int:event_id>&<int:addition_num>', methods=['GET', 'POST'])
@login_required
def del_event_addition(event_id, addition_num):
    session = db_session.create_session()
    event = session.query(Event).get(event_id)
    if current_user.id != event.user_id:
        abort(403)
    additions = event.additions.split('$')
    if len(additions) <= addition_num:
        abort(404)
    del additions[addition_num]
    event.additions = '$'.join(additions)
    session.commit()
    return redirect(f'/event/{event_id}')


@blueprint.route('/del_event/<int:event_id>', methods=['GET', 'POST'])
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
