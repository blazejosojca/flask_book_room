import unittest
import os
from mysql import connector

from flask import current_app, url_for
from flask_testing import TestCase
from flask_login import current_user

from app import create_app, db
from config import TestingConfig, Config, BASEDIR

from app.models import User, Room, Booking, Department, Position
from app.auth.routes import login
from app.auth.routes import current_user
from app.department.routes import create_department
from app.tests.test_data import TestData as td


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


class TestServer(BaseTest):

    def test_server_is_up(self):
        tester = current_app.test_client()
        response = tester.get(url_for('main.home'))
        self.assertEqual(response.status_code, 200)

    def test_database_exist(self):
        cnx = connector.connect(host='localhost',
                                database='bookings_test',
                                user='root',
                                password='password'
                                )
        self.assertTrue(cnx)


class TestModels(BaseTest):

    def test_empty_user_model(self):
        self.assertEqual(User.query.count(), 0)

    def test_empty_room_model(self):
        self.assertEqual(Room.query.count(), 0)

    def test_empty_reservation_model(self):
        self.assertEqual(Booking.query.count(), 0)

    def test_empty_department_model(self):
        self.assertEqual(Department.query.count(), 0)

    def test_empty_position_model(self):
        self.assertEqual(Position.query.count(), 0)


class TestRoutes(BaseTest):
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('main/home.html')

    def test_register_page(self):
        response = self.app.get(url_for('auth.register'),
        follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('auth/register.html')
        
    def test_login_page(self):
        response = self.app.get(url_for('auth.login'),
        follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('auth/login.html')


class TestRegistration(BaseTest):
    def test_registration_new_user_with_valid_data(self):
        response = self.register(td.TEST_FIRST_NAME, td.TEST_SECOND_NAME, td.TEST_MOBILE_PHONE, 'new_test@mail.com', td.TEST_PASSWORD, td.TEST_PASSWORD)
        user = User.query.all()
        self.assert200(response)
        print(user[0])
        self.assertEqual(1, len(user))

class TestDepartment(BaseTest):
    def test_add_new_department(self):
        self.app.post('/department/new', data=dict(
            department_name=td.TEST_DEPARTMENT_NAME
        ))
        dep_list = Department.query.all()

        self.assertEqual(1, len(dep_list))
        

    def test_remove_existing_department(self):
        pass

    def test_list_existing_department(self):
        pass

    def test_edit_existing_department(self):
        pass

if __name__ == '__main__':
    unittest.main()
