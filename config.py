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
    USE_RELOADER = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    ENV = 'testing'
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/booking_test'
