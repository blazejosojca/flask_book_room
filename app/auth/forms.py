""" importing flask modules, internal app modules """
from flask_babel import _, lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo, Required
from app.models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=2, max=36)])
    second_name = StringField('Second name', validators=[DataRequired(), Length(min=2, max=36)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmation = PasswordField(_l('Confirm Password', validators=[DataRequired(), EqualTo('password')]))
    submit = SubmitField('Sign Up!')

    def validate_user_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                _l('This username already exists. Please use a different email!'))


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))

