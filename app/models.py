from app import db, login
from flask_login import UserMixin
from werkzeug.security import (generate_password_hash,
                               check_password_hash)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    second_name = db.Column(db.String(64), nullable=False)
    


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

