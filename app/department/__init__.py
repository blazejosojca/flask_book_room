from flask import Blueprint

bp = Blueprint('department', __name__)

from app.bookings import routes