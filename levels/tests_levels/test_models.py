from django.test import TestCase
from ..models import Level


class TestLevelModel(TestCase):
    def setUp(self):
        self.level_data = {
            "name": "floor 1",
            "fill_priority": 2,
            "bike_spots": 1,
            "car_spots": 2
        }

    def test_must_create_new_level(self):
        level = Level.objects.create(**self.level_data)
        level = Level.objects.first()
        self.assertEqual(
            level.name,
            self.level_data['name'],
            msg='I was unable to create a new level.'
        )
