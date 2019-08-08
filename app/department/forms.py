from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class DepartmentForm(FlaskForm):
    name = StringField(_('Enter name of department', validators=[DataRequired()]))
    submit = SubmitField(_("Done!"))