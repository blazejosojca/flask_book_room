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
# @login_required
def create_room():
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
    return render_template('rooms/create_room.html', title=create_room, form=form, legend='New room')


@bp.route('/room/list', methods=['GET', 'POST'])
# @login_required
def list_rooms():
    rooms = Room.query.all()
    return render_template('rooms/list_rooms.html', rooms=rooms)

@bp.route('/room/<int:room_id>', methods=['GET', 'POST'])
# @login_required
def details_room(room_id):
    room = Room.query.get_or_404(room_id)
    return render_template('rooms/view_room.html', room=room)


@bp.route('/room/update/<int:room_id>', methods=['GET', 'POST'])
#@login_required
def update_room(room_id):
    pass


@bp.route('/room/delete/<int:room_id>', methods=['GET', 'PATCH'])
#@login_required
def delete_room(room_id):
    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    flash('Room has been deleted !. Database is up to date!')
    return redirect(url_for('main.home'))
