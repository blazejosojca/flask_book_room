import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ENV = 'development'
    TESTING = False
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'hard_to_guess_12345678'
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/bookings_db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
