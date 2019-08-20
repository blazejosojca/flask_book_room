from flask import url_for, render_template, flash, request
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
    form = RoomForm()
    if form.validate_on_submit():
        room = Room(
            name=form.name.data,
            seats=form.seats.data,
            floor=form.floor.data,
            projector=form.projector.data,
            air_condition=form.air_condition.data,
            whiteboard=form.whiteboard.data
        )
        db.session.add(room)
        db.session.commit()
        flash(_('New room was added to database'))
        return redirect(url_for('rooms.list_rooms'))
    return render_template('rooms/create_room.html', title=create_room, form=form, legend='New room')


@bp.route('/room/list', methods=['GET', 'POST'])
def list_rooms():
    rooms = Room.query.all()
    return render_template('rooms/list_rooms.html', rooms=rooms, title='List of rooms',
                           legend='Rooms')


@bp.route('/room/<int:room_id>', methods=['GET', 'POST'])
def room_details(room_id):
    room = Room.query.get_or_404(room_id)
    air_condition = room.has_air_condition()
    projector = room.has_projector()
    whiteboard = room.has_whiteboard()

    return render_template('rooms/view_room.html', room=room,
                           air_condition=air_condition,
                           projector=projector,
                           whiteboard=whiteboard,
                           title='Room details',
                           legend='Room')

@bp.route('/room/update/<int:room_id>', methods=['GET', 'POST'])
@login_required
def update_room(room_id):
    room = Room.query.get_or_404(room_id)
    form = RoomForm()
    if form.validate_on_submit():
        room.name = form.name.data
        room.capacity = form.capacity.data
        room.floor = form.floor.data
        room.seats = form.seats.data
        room.projector = form.projector.data
        room.air_condition = form.air_condition.data
        room.whiteboard = form.whiteboard.data
        db.session.commit()
        flash(_('Room info has been updated!'))
        return redirect(url_for('rooms.list_rooms'))
    elif request.method == 'GET':
        room.name = form.name
        room.capacity = form.capacity
        room.floor = form.floor
        room.seats = form.seats
        room.projector = form.projector
        room.air_condition = form.air_condition
        room.whiteboard = form.whiteboard
    return render_template('rooms/create_room.html',
                           title='Update room info',
                           form=form, legend='Update room info')


@bp.route('/room/delete/<int:room_id>', methods=['POST', 'GET'])
@login_required
def delete_room(room_id):
    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    flash('Room has been deleted !')
    return redirect(url_for('rooms.list_rooms'))
