from app import db, login

from flask_login import UserMixin
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from datetime import datetime


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    second_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    mobile_phone = db.Column(db.String(64), nullable=False,unique=True)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    bookings = db.relationship('Booking', backref='host', lazy='dynamic')
    password_hashed = db.Column(db.String(128), nullable=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())
    
    def set_password(self, password):
        self.password_hashed = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hashed, password)

    def get_user_full_name(self):
        return '{} {}'.format(self.first_name, self.second_name)

    def to_dict(self, include_email=False):
        data ={
            'id': self.id,
            'first_name':self.first_name,
            'second_name':self.second_name,
            'mobile_phone':self.mobile_phone,
            'position_id':self.position_id,
            'department_id':self.department_id,
            'bookings':self.bookings.count(),
            'last_seen':self.last_seen.isoformat() + 'Z',
        }
        if include_email:
            data['email'] = self.email
        return data
    
    def from_dict(self, data, new_user=False):
        for field in ['first_name', 'last_name', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])


    def __repr__(self):
        return '<User: {} {} / {}/ {} >'.format(self.first_name, self.second_name, self.department, self.email)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String(64), nullable=False, unique=True)
    employers = db.relationship('User', backref='position', lazy='dynamic')

    def __repr__(self):
        return 'Position {}'.format(self.position_name)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.String(128))
    members = db.relationship('User', backref='department', lazy='dynamic')

    def __repr__(self):
        return 'Department {}'.format(self.department_name)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.Integer, default=2)
    projector = db.Column(db.Boolean, default=False)
    air_condition = db.Column(db.Boolean, default=False)
    whiteboard = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '< Room: {} >'.format(self.name)
    
    def extended_room_info(self):
        return '< Room: {}, seats {}, floor {}>'.format(self.name, self.seats, self.floor)
    
    def has_projector(self):
        if self.projector:
            status = "Yes"
        else:
            status = "No"
        return status

    def has_air_condition(self):
        if self.air_condition:
            status = "Yes"
        else:
            status = "No"
        return status

    def has_whiteboard(self):
        if self.whiteboard:
            status = "Yes"
        else:
            status = "No"
        return status


class Booking(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    meeting_title = db.Column(db.String(64))
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    meeting_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(128), nullable=True)

    def user_name(self):
        user = User.query.get(load_user)
        full_name = '{} {}'.format(user.first_name, user.second_name)
        return full_name

    def __repr__(self):
        return '<Booking: {} reserved {} on {} >'.format(self.host_id, self.room_id, self.meeting_date)
