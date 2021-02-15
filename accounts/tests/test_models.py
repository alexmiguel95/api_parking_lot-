from django.test import TestCase
from django.contrib.auth.models import User


class TestUserModel(TestCase):
    def setUp(self):
        self.admin_data = {
            "username": "admin",
            "password": "123456789",
            "is_staff": True,
            "is_superuser": True
        }

    def test_must_create_new_super_user(self):
        admin = User.objects.create_user(**self.admin_data)
        admin = User.objects.first()
        self.assertEqual(admin.username, self.admin_data['username'])
        self.assertEqual(admin.is_superuser, True)
