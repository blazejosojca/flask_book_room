from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField


class BookingForm(FlaskForm):
    booking_date = DateField('Date of booking', validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Length(max=130)])
    submit = SubmitField(_("Done!"))
