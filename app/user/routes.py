from flask import url_for, render_template, redirect, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import User
from app.user import bp
from app.auth.forms import RegistrationForm, LoginForm

@bp.route('user/edit/<int:user_id>')
@login_required
def edit_user():
    pass

@bp.route('user/<int:user_id>')
def user_details():
    pass

@bp.route('user/list')
def list_users():
    pass

@bp.route('user/delete/<int:user_id>')
@login_required
def delete_user():
    pass

