from flask import current_app
from app import db, login
from flask_login import UserMixin
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from datetime import date, datetime


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    second_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hashed = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())
    
    def set_password(self, password):
        self.password_hashed = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hashed, password)
        
    def __repr__(self):
        return '<User: {} {} - {}>'.format(self.first_name, self.second_name, self.email)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    capacity = db.Column(db.Integer, default=1)
    has_projector = db.Column(db.Boolean, default=False)
    has_air_condition = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '< Room: {}>'.format(self.name)


class Reservation(db.Model):
    """In this model booking_date is a day when user make the reservation.
     And reservation_date is a date of day when user want to use the room."""
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), primary_key=True, nullable=False)
    booking_date= db.Column(db.Date, nullable=False, default=datetime.utcnow())
    reservation_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(128), nullable=True)
    reserved = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return '<Reservation: {} reserved {} on {} >'.format(self.user_id, self.room_id, self.reservation_date)
