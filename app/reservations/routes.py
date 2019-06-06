
from datetime import datetime
from flask import url_for, render_template, flash
from flask_login import current_user, login_required

from werkzeug.utils import redirect

from app import db
from app.models import Reservation, Room
from app.reservations import bp
from app.reservations.forms import ReservationForm


@bp.route('/reservations/<int:room_id>', methods=['POST', 'GET'])
@login_required
def make_reservation(room_id):
    form = ReservationForm()
    room = Room.query.filter_by(id=room_id).first()
    if form.validate_on_submit():
        reservation = Reservation(
            user_id=current_user.id,
            room_id=room_id,
            booking_date=datetime.utcnow(),
            reservation_date=form.reservation_date.data,
            description=form.description.data,
            reserved=True,
        )
        db.session.add(reservation)
        db.session.commit()

        flash('Reservation has been made')
        return redirect(url_for('rooms.list_rooms'))
    return render_template('reservations/reservation.html',
                           title='make_reservation',
                           form=form,
                           legend='New reservation',
                           room=room,
                           user=current_user)


@bp.route('/reservation/<int:reservation_id>', methods=['GET', 'POST'])
@login_required
def view_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)

    return render_template('reservation/view_reservation.html', reservation=reservation)



@bp.route('/reservation/delete/<int:reservation_id>', methods=['GET', 'POST'])
def delete_reservation():
    pass


@bp.route('/reservation/list/<int:room_id>', methods=['GET', 'POST'])
def list_reservation_for_room():
    pass


@bp.route('/reservation/list/<int:user_id>', methods=['GET', 'POST'])
def list_reservation_for_user():
    pass


@bp.route('/reservation/update/<int:reservation_id>', methods=['GET', 'POST'])
def update_reservation():
    pass


@bp.context_processor
def inject_now():
    return {'now': datetime.utcnow()}
