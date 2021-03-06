
from datetime import datetime
from flask import url_for, render_template, flash, abort
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
            host_id=current_user.id,
            room_id=room_id,
            booking_date=datetime.utcnow(),
            meeting_title=form.meeting_title.data,
            meeting_date=form.meeting_date.data,
            description=form.description.data,
        )
        db.session.add(reservation)
        db.session.commit()

        flash('Reservation has been made')
        return redirect(url_for('rooms.list_rooms'))
    return render_template('booking/create_booking.html',
                           title='make_reservation',
                           form=form,
                           legend='New booking',
                           room=room,
                           user=current_user)


@bp.route('/booking/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def view_booking(booking_id):
    booking = Booking.query.get(booking_id)
    return render_template('booking/create_booking.html', booking=booking)

@bp.route('/booking/delete/<int:booking_id>', methods=['GET', 'POST'])
def delete_booking(booking_id):
    booking = Booking.query.get(booking_id)
    db.session.delete(booking)
    db.session.commit()
    flash('Booking has been removed !')
    return redirect(url_for('booking.view_booking'))

@bp.route('/booking/list', methods=['GET', 'POST'])
def list_all_bookings():
    bookings = Booking.query.all()
    return render_template('booking/list_bookings.html', bookings=bookings)

@bp.route('/booking/list/<int:room_id>', methods=['GET', 'POST'])
def list_bookings_for_room(room_id):
    bookings_for_room = Booking.query.filter_by(room_id=room_id)
    render_template('booking/list_bookings.html', bookings=bookings_for_room)


@bp.route('/booking/list/<int:host_id>', methods=['GET', 'POST'])
def list_bookings_for_user(host_id):
    bookings_for_host = Booking.query.filter_by(host_id=host_id)
    render_template('booking/list_bookings.html', bookings=bookings_for_host)


@bp.route('/booking/update/<int:booking_id>', methods=['GET', 'POST'])
def update_bookings(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.host_id != current_user:
        abort(403)
    form = BookingForm()
    if form.validate_on_submit():
        booking.room_id = form.room_id.data,
        booking.booking_date = datetime.utcnow(),
        booking.meeting_title = form.meeting_title.data,
        booking.description = form.description.data,




@bp.context_processor
def inject_now():
    return {'now': datetime.utcnow()}
