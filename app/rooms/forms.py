from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

from app.models import Reservation


class RoomForm(FlaskForm):
    date_of_booking = DateField(_('DateOfBooking'), validators=DataRequired())
    description = StringField(_('Capacity'), alidators=[DataRequired(), Length(min=3, max=60)])
    submit = SubmitField(_("Done!"))


