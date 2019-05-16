import os
from datetime import datetime
from flask import url_for, render_template, flash, request, abort
from flask_login import current_user, login_required
from flask_babel import _, lazy_gettext as _l
from werkzeug.utils import redirect

from app import db
from app.models import Reservation, User,Room
from app.reservations import bp
from app.admin.routes import check_admin
from app.reservations.forms import ReservationForm

@bp.route('/reservations/<int:room_id>', methods=['GET', 'POST'])
@login_required
def make_reservation(room_id):
    form = ReservationForm()
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        reservation=Reservation(
            user_id=user,
            room_id=room_id,
            datetime_of_booking=datetime.utcnow(),
            booking_date=form.booking_date.data,
            description = form.description.data
        )
        db.session.add(reservation)
        db.session.commit()
        flash(_('Reservation has been made'))
        return redirect(url_for('rooms.list_rooms'))
    return render_template('rooms/create_room.html', title='create_room', form=form, legend='New room')

@bp.route('/reservation/<int:reservation_id>', methods=['GET', 'POST'])
def view_reservation():
    pass

@bp.route('/reservation/delete/<int:reservation_id>', methods=['GET', 'POST'])
def delete_reservation():
    pass

@bp.route('/reservation/list', methods=['GET', 'POST'])
def list_reservation():
    pass

@bp.route('/reservation/update/<int:reservation_id>', methods=['GET', 'POST'])
def update_reservation():
    pass
