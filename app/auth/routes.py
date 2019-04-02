from flask import url_for, render_template, redirect, flash, request
from flask_login import current_user, login_user, logout_user
from flask_babel import _, lazy_gettext as _l

from app import db
from app.models import User
from app.auth import bp
from app.auth.forms import RegistrationForm, LoginForm


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            second_name=form.second_name.data,
            email=form.email.data,
            mobile_phone=form.mobile_phone.data
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash(_l("A new user added. Congratulations!"), 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(
            email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid credentials!", 'info')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember.data)
        flash('WOW')
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', title='Login', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

