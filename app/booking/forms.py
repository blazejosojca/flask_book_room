from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField


class BookingForm(FlaskForm):
    title = StringField(_('Meeting title:', validators=[]))
    meeting_date = DateField(_('Date of meeting', validators=[DataRequired()]))
    description = TextAreaField(_("Description", validators=[Length(max=130)]))
    submit = SubmitField(_("Done!"))
