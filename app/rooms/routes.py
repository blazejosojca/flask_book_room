import os

from flask import url_for, render_template, flash, request, abort
from flask_login import current_user, login_required
from flask_babel import _, lazy_gettext as _l
from werkzeug.utils import redirect

from app import db
from app.models import Room
from app.rooms import bp
from app.rooms.forms import CreateRoomForm, UpdateRoomForm

@bp.route('/room/new', methods)