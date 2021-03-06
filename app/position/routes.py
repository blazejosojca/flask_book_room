
from datetime import datetime
from flask import url_for, render_template, flash
from flask_login import current_user, login_required

from werkzeug.utils import redirect

from app import db
from app.models import Booking, Room
from app.booking import bp
from app.booking.forms import BookingForm


@bp.route('/booking/<int:room_id>', methods=['POST', 'GET'])
@login_required
def make_booking(room_id):
    form = BookingForm()
    room = Room.query.filter_by(id=room_id).first()
    if form.validate_on_submit():
        reservation = Booking(
            user_id=current_user.id,
            room_id=room_id,
            booking_date=datetime.utcnow(),
            reservation_date=form.booking_date.data,
            description=form.description.data,
            reserved=True,
        )
        db.session.add(reservation)
        db.session.commit()

        flash('Reservation has been made')
        return redirect(url_for('rooms.list_rooms'))
    return render_template('booking/create_booking.html',
                           title='make_reservation',
                           form=form,
                           legend='New reservation',
                           room=room,
                           user=current_user)


@bp.route('/booking/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def view_booking(booking_id):
    pass
    # reservation = Booking.query.get(reservation_id)
    #
    # return render_template('booking/create_booking.html.html', booking=booking)



@bp.route('/booking/delete/<int:booking_id>', methods=['GET', 'POST'])
def delete_booking():
    pass


@bp.route('/booking/list/<int:room_id>', methods=['GET', 'POST'])
def list_bookings_for_room():
    pass


@bp.route('/booking/list/<int:user_id>', methods=['GET', 'POST'])
def list_bookings_for_user():
    pass


@bp.route('/booking/update/<int:booking_id>', methods=['GET', 'POST'])
def update_bookings():
    pass


@bp.context_processor
def inject_now():
    return {'now': datetime.utcnow()}
