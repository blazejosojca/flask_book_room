from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo

from app.models import Room


class RoomForm(FlaskForm):
    name = StringField(_('Name'), validators=[DataRequired(), Length(min=3, max=60)])
    capacity = IntegerField(_('Capacity'), validators=[DataRequired()])
    projector = BooleanField(_("Projector"), validators=[DataRequired()])
    air_condition = BooleanField(_("Air condition"), validators=[DataRequired()])
    submit = SubmitField(_("Done!"))

