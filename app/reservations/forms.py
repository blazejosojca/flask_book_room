from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo

from app.models import Reservation


class ReservationForm(FlaskForm):
    user = StringField(_('Host'), validators=[DataRequired])
    room = IntegerField()
    today = IntegerField()
    date_ = IntegerField()

    submit = SubmitField(_("Done!"))


