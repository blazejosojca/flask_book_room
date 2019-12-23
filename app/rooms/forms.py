from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

from app.models import Room


class RoomForm(FlaskForm):
    name = StringField(_('Name'), validators=[DataRequired(), Length(min=3, max=60)])
    seats = IntegerField(_('Capacity'), validators=[DataRequired(), NumberRange(1, 99)])
    floor = IntegerField(_('Floor'), validators=[DataRequired(), NumberRange(0, 10)])
    projector = BooleanField(_("Projector"))
    air_condition = BooleanField(_("Air condition"))
    whiteboard = BooleanField(_("Whiteboard"))
    submit = SubmitField(_("Done!"))


