from app import db, login
from flask_login import UserMixin
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from datetime import date, datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    second_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    mobile_phone = db.Column(db.String(9), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return '<User: {} - {} {} - {}>'.format(self.username, self.first_name, self.second_name, self.email)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    capacity = db.Column(db.Integer, default=1)
    has_projector = db.Column(db.Boolean, default=False)
    has_air_condition = db.Column(db.Boolean, default=False)
    
    
    def __repr__(self):
        return '< Room: {}>'.format(self.name)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    datetime_of_booking = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    booking_date = db.Column(db.Date, nullable=False)
    
    is_reservation = db.Column(db.Boolean, default=False)
    
    
    def __repr__(self):
        return '<Reservation: {} reserved {} {} >'.format(self.user_id, self.room_id, self.date_reservation)
    
    

    
    
    
    

