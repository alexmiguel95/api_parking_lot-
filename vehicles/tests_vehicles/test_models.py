from django.test import TestCase
from ..models import Pricing


class TestPrincingModel(TestCase):
    def setUp(self):
        self.pricing_data = {
            "a_coefficient": 100,
            "b_coefficient": 100
        }

    def test_must_create_new_princing(self):
        pricing = Pricing.objects.create(**self.pricing_data)
        pricing = Pricing.objects.first()
        self.assertEqual(
            pricing.a_coefficient,
            self.pricing_data['a_coefficient'],
            msg='I was unable to create the coefficients.'
        )
        self.assertEqual(
            pricing.b_coefficient,
            self.pricing_data['b_coefficient'],
            msg='I was unable to create the coefficients.'
        )
