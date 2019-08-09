from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l

from config import Config, DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap()
login.login_view = 'auth.login'
login.login_message = _l("Please log in to view this page.")
babel = Babel()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)
    # mail.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)

    from app import models
    from app.auth import bp as auth_bp
    from app.errors import bp as errors_bp
    from app.main import bp as main_bp
    from app.rooms import bp as rooms_bp
    from app.booking import bp as bookings_bo
    from app.department import bp as department_bo
    from app.position import bp as position_bo

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(errors_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(rooms_bp)
    app.register_blueprint(bookings_bo)
    app.register_blueprint(department_bo)

    return app
