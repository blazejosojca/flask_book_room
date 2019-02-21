import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


from config import Config, DevelopmentConfig


app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page'
mail = Mail()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)

    from app.auth import bp as auth_bp
    from app.admin import bp as admin_bp
    from app.errors import bp as errors_bp
    from app.main import bp as main_bp
    from app.rooms import bp as rooms_bp

    app.register_blueprint(auth_bp, url_prefix = '/auth')
    app.register_blueprint(admin_bp, url_prefix = '/dmin')
    app.register_blueprint(errors_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(rooms_bp)

    return app
