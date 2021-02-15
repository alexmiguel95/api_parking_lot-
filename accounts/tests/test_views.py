from django.test import TestCase
from rest_framework.test import APIClient


class TestAccountView(TestCase):
    def setUp(self):
        self.admin_data = {
            "username": "admin",
            "password": "123456789",
            "is_staff": True,
            "is_superuser": True
        }

        self.admin_data_login = {
            "username": "admin",
            "password": "123456789"
        }

    def test_create_and_login_super_user(self):
        client = APIClient()

        # Test the creted account
        user = client.post(
            '/api/accounts/', self.admin_data, format='json').json()

        self.assertEqual(
            user,
            {
                'id': 1,
                "username": "admin",
                "is_superuser": True,
                "is_staff": True
            },
            msg="""Parameters incorrect. Mandatory: username, password,
            is_superuser, is_staff."""
        )

        # Test the login
        response = client.post(
           '/api/login/', self.admin_data_login, format='json').json()

        self.assertIn(
            "token",
            response.keys(),
            msg="Invalid username or password"
        )
