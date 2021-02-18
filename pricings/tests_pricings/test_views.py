from django.test import TestCase
from rest_framework.test import APIClient


class TestCreatePricing(TestCase):
    def setUp(self):
        self.pricing_data = {
            "a_coefficient": 100,
            "b_coefficient": 100
        }

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

        self.user_common_data = {
            "username": "usercommon",
            "password": "123456789",
            "is_staff": False,
            "is_superuser": False
        }

        self.user_common_data_login = {
            "username": "usercommon",
            "password": "123456789"
        }

    def test_must_create_a_new_pricing(self):
        client = APIClient()

        # You must not allow the creation of a nine level without being
        # authenticated as an administrator user.
        client.post('/api/accounts/', self.user_common_data, format='json')

        # Get token user common
        token = client.post(
            '/api/login/', self.user_common_data_login, format='json'
        ).json()['token']

        client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = client.post(
           '/api/pricings/', self.pricing_data, format='json')
        self.assertTrue(response.status_code, 403)

        # Create a new level with an admin user
        client.post('/api/accounts/', self.admin_data, format='json')

        # Get token user admin
        token = client.post(
            '/api/login/', self.admin_data_login, format='json'
        ).json()['token']

        client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = client.post(
           '/api/pricings/', self.pricing_data, format='json')
        self.assertTrue(response.status_code, 201)
