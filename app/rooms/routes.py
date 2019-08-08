import os

from flask import url_for, render_template, flash, request, abort
from flask_login import current_user, login_required
from flask_babel import _, lazy_gettext as _l
from werkzeug.utils import redirect

from app import db
from app.models import Room
from app.rooms import bp
from app.rooms.forms import RoomForm



@bp.route('/room/new', methods=['GET', 'POST'])
@login_required
def create_room():
    # check_admin()
    form = RoomForm()
    if form.validate_on_submit():
        room=Room(
            name=form.name.data,
            capacity=form.capacity.data,
            has_projector=form.projector.data,
            has_air_condition=form.air_condition.data
        )
        db.session.add(room)
        db.session.commit()
        flash(_('New room was added to database'))
        return redirect(url_for('rooms.list_rooms'))
    return render_template('rooms/create_room.html', title=create_room, form=form, legend='New room')


@bp.route('/room/list', methods=['GET', 'POST'])
@login_required
def list_rooms():
    rooms = Room.query.all()
    return render_template('rooms/list_rooms.html', rooms=rooms)

@bp.route('/room/<int:room_id>', methods=['GET', 'POST'])
@login_required
def details_room(room_id):
    room = Room.query.get_or_404(room_id)
    air_condition = room.has_air_condition_info()
    projector = room.has_projector_info()

    return render_template('rooms/view_room.html', room=room, air_condition=air_condition, projector=projector)

#TODO
@bp.route('/room/update/<int:room_id>', methods=['GET', 'POST'])
@login_required
def update_room(room_id):
    room = Room.query.get_or_404(room_id)
    form = RoomForm()
    if form.validate_on_submit():
        room.name = form.name.data
        room.capacity = form.capacity.data
        room.has_projector = form.has_projector.data
        room.has_air_condition = form.has_air_condition.data
        db.session.commit()
        flash(_('Room info has been updated!'))
        return redirect(url_for('rooms.list_rooms'))
    elif request.method == 'GET':
        room.name = form.name
        room.capacity = form.capacity
        room.has_projector = form.has_projector
        room.has_air_condition = form.has_air_condition
    return render_template('rooms/create_room.html',
                           title='Update room info',
                           form=form, legend='Update room info')

#TODO
@bp.route('/room/delete/<int:room_id>', methods=['POST', 'GET'])
@login_required
def delete_room(room_id):
    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    flash('Room has been deleted ! Database is up to date!')
    return redirect(url_for('rooms.list_rooms'))

