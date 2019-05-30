from flask import render_template

from app.main import bp
from app.models import Room

@bp.route("/")
@bp.route("/home")
def home():
    rooms = Room.query.all()
    return render_template("main/home.html", title = 'Home', rooms=rooms)
