from flask import abort, render_template
from flask_login import current_user, login_required

from app.admin import bp
from app.models import User

def check_admin():
    if not current_user.is_admin:
        abort(403)