from flask import render_template, current_app
from app import db
from app.errors import bp


@bp.app_errorhandler(403)
def no_permission_error(error):
    return render_template('errors/403.html', title='Forbidden'), 403


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', title='Lost in the woods'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', title='Server is broken! OMG!'), 500
