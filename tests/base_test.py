import unittest
import os
from flask import url_for, current_app

from flask_testing import TestCase

from app import create_app, db
from config import TestingConfig


class BaseTest(TestCase):

    def create_app(self):
        app = create_app(TestingConfig)

        return app

    def setUp(self):
        self.app = current_app.test_client()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def register(self, first_name, second_name, mobile_phone, email, password, password_confirmation):
        return self.app.post(
            '/auth/register',
            data=dict(
                first_name=first_name,
                second_name=second_name,
                mobile_phone=mobile_phone,
                email=email,
                password=password,
                password_confirmation=password_confirmation),
            follow_redirects=True)

    def login(self, email, password):
        return self.app.post(
            '/auth/login',
            data=dict(
                email=email,
                password=password),
            follow_redirect=True)

    def logout(self):
        return self.app.get('/logout',
                            follow_redirect=True)

