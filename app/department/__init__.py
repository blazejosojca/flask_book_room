from flask import Blueprint

bp = Blueprint('department', __name__)

from app.department import routes, forms