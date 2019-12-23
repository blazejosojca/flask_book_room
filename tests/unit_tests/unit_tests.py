import unittest
from mysql import connector

from flask import current_app, url_for

from app.models import User, Room, Booking, Department, Position
from tests.test_data import TestData as td
from tests.base_test import BaseTest



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
    def test_valid_user_registration(self):
        response = self.register(td.TEST_FIRST_NAME, td.TEST_SECOND_NAME, td.TEST_MOBILE_PHONE, 'new_test@mail.com', td.TEST_PASSWORD, td.TEST_PASSWORD)
        user = User.query.all()
        self.assert200(response)
        self.assertEqual(1, len(user))

    def test_invalid_user_registration_different_password(self):
        response = self.register(td.TEST_FIRST_NAME,
                                 td.TEST_SECOND_NAME,
                                 td.TEST_MOBILE_PHONE,
                                 'new_test@mail.com',
                                 td.TEST_PASSWORD,
                                 'TEST_PASSWORD')
        self.assertIn(b'Field must be equal to password', response.data)

    def test_invalid_user_registration_unique_user(self):
        values = (td.TEST_FIRST_NAME,
                td.TEST_SECOND_NAME,
                td.TEST_MOBILE_PHONE,
                'new_test@mail.com',
                td.TEST_PASSWORD,
                'TEST_PASSWORD')
        self.register(*values)
        response = self.register(*values)
        self.assertIn(b'Email already exists. Use a different email!', response.data)


class TestLogin(BaseTest):
    Email = 'new_test@mail.com'
    DATA = (td.TEST_FIRST_NAME, td.TEST_SECOND_NAME, td.TEST_MOBILE_PHONE, Email, td.TEST_PASSWORD, td.TEST_PASSWORD)
    def test_login_valid_credentials(self):
        self.register(*self.DATA)
        # response = self.login('new_test@mail.com, ')user = User.query.all()
        response = self.login(self.Email, td.TEST_PASSWORD)
        self.assertEqual(response.status_code, 301)


    def test_login_empty_credentials(self):
        pass

    def test_login_invalid_password(self):
        pass

    def test_login_invalid_email(self):
        pass


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
