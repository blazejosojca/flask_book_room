from flask import Blueprint

bp = Blueprint('department', __name__)

from app.booking import routes