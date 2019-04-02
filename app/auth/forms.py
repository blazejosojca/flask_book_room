""" importing flask modules, internal app modules """
from flask_babel import _, lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo

from app.models import User

class RegistrationForm(FlaskForm):
    first_name = StringField(_l('First name', validators=[DataRequired(), Length(min=2, max=36)]))
    second_name = StringField(_l('Second name', validators=[DataRequired(), Length(min=2, max=36)]))
    mobile_phone = StringField(_l('Mobile phone', validators=[DataRequired(), Length(min=9, max=13)]))
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password', validators=[DataRequired()]))
    password_confirmation = PasswordField(_l('Confirm Password', validators=[DataRequired(), EqualTo('password')]))
    submit = SubmitField(_l('Sign Up!'))

    def validate_user_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                _l('This username already exists. Please use a different email!'))

    def validate_user_mobile_phone(self, mobile_phone):
        user = User.query.filter_by(mobile_phone=mobile_phone.data).first()
        if user is not None:
            raise ValidationError(
                _l('User with this mobilephone exists. Please use a different mobilephone!'))


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))

