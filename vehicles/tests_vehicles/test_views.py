from django.test import TestCase
from rest_framework.test import APIClient


class TestCreateVeihcle(TestCase):
    def setUp(self):
        self.vehicle_data = {
            "vehicle_type": "car",
            "license_plate": "AYO1030"
        }

        self.pricing_data = {
            "a_coefficient": 100,
            "b_coefficient": 100
        }

        self.level1_data = {
            "name": "floor 1",
            "fill_priority": 2,
            "bike_spots": 1,
            "car_spots": 2
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

    def test_must_create_a_new_vehicle(self):
        client = APIClient()

        # Try to create a vehicle without having a light and registered price.
        # A 404 is expected.
        vehicle = client.post(
           '/api/vehicles/', self.vehicle_data, format='json')
        self.assertEqual(vehicle.status_code, 404)

        # Create a new level with an admin user
        client.post('/api/accounts/', self.admin_data, format='json')

        # Get token user admin
        token = client.post(
            '/api/login/', self.admin_data_login, format='json'
        ).json()['token']

        client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = client.post(
           '/api/levels/', self.level1_data, format='json')
        self.assertTrue(response.status_code, 201)

        # Create pricing
        response = client.post(
           '/api/pricings/', self.pricing_data, format='json')
        self.assertTrue(response.status_code, 201)

        # Create vehicle
        vehicle = client.post(
           '/api/vehicles/', self.vehicle_data, format='json')
        self.assertEqual(vehicle.status_code, 201)

        vehicle = vehicle.json()
        self.assertEqual(
            vehicle["license_plate"], self.vehicle_data['license_plate']
        )
