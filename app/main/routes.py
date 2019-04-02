from flask import render_template, url_for, redirect
from flask_login import current_user

from app.main import bp

@bp.route("/")
@bp.route("/home")
def home():
    return render_template("main/home.html", title = 'Home')
