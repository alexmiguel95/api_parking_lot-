from django.test import TestCase
from vehicles.models import Vehicle


class TestVehicleModel(TestCase):
    def setUp(self):
        self.vehicle_data = {
            "vehicle_type": "car",
            "license_plate": "AYO1030"
        }

    def test_must_create_new_princing(self):
        vehicle = Vehicle.objects.create(**self.vehicle_data)
        vehicle = Vehicle.objects.first()
        self.assertEqual(
            vehicle.license_plate,
            self.vehicle_data['license_plate'],
            msg='I was unable to create the vehicle.'
        )
