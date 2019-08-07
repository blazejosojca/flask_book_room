
from datetime import datetime
from flask import url_for, render_template, flash
from flask_login import current_user, login_required

from werkzeug.utils import redirect

from app import db
from app.models import Booking, Room
from app.booking import bp
from app.booking.forms import BookingForm


@bp.route('/department/<int:dep_id>', methods=['POST', 'GET'])
@login_required
def add_department(room_id):
    pass


@bp.route('/booking/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def view_depart(booking_id):
    
    reservation = Booking.query.get(reservation_id)

    return render_template('booking/booking.html.html', booking=booking)



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
