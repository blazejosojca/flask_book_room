

from app.models import User
from tests.test_data import TestData as td
from tests.base_test import BaseTest


class TestRegistration(BaseTest):

    def test_registration_new_user_with_valid_data(self):
        response = self.register(td.TEST_FIRST_NAME, td.TEST_SECOND_NAME, td.TEST_MOBILE_PHONE, 'new_test@mail.com', td.TEST_PASSWORD, td.TEST_PASSWORD)
        user = User.query.all()
        self.assert200(response)
        print(user[0])
        self.assertEqual(1, len(user))