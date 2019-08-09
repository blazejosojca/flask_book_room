from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class DepartmentForm(FlaskForm):
    name = StringField(_('Enter name of department', validators=[DataRequired(), Length(60)]))
    description = StringField(_('Short description', validators=[DataRequired(), Length(120)]))
    submit = SubmitField(_('Done!'))