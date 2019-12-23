""" importing flask modules, internal app modules """
from flask_babel import _, lazy_gettext as _l
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=2, max=36)])
    second_name = StringField('Second name', validators=[DataRequired(), Length(min=2, max=36)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mobile_phone = StringField('Mobile', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up!')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(
                'Email already exists. Use a different email!')

    def validate_mobile_phone(self, mobile_phone):
        if User.query.filter_by(email=mobile_phone.data).first():
            raise ValidationError(
                'This mobile number already exists. Use a different number!')
        



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))

