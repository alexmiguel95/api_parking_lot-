# from django.test import TestCase
# from rest_framework.test import APIClient


# class TestCreateLevel(TestCase):
#     def setUp(self):
#         self.level1_data = {
#             "name": "floor 1",
#             "fill_priority": 2,
#             "bike_spots": 1,
#             "car_spots": 2
#         }

#         self.level2_data = {
#             "name": "floor 2",
#             "fill_priority": 1,
#             "bike_spots": 3,
#             "car_spots": 4
#         }

#         self.admin_data = {
#             "username": "admin",
#             "password": "123456789",
#             "is_staff": True,
#             "is_superuser": True
#         }

#         self.admin_data_login = {
#             "username": "admin",
#             "password": "123456789"
#         }

#         self.user_common_data = {
#             "username": "usercommon",
#             "password": "123456789",
#             "is_staff": False,
#             "is_superuser": False
#         }

#         self.user_common_data_login = {
#             "username": "usercommon",
#             "password": "123456789"
#         }

#     def test_must_create_a_new_level(self):
#         client = APIClient()

#         # You must not allow the creation of a nine level without being
#         # authenticated as an administrator user.
#         client.post('/api/accounts/', self.user_common_data, format='json')

#         # Get token user common
#         token = client.post(
#             '/api/login/', self.user_common_data_login, format='json'
#         ).json()['token']

#         client.credentials(HTTP_AUTHORIZATION='Token ' + token)

#         response = client.post(
#            '/api/levels/', self.level1_data, format='json')
#         self.assertTrue(response.status_code, 403)

#         # Create a new level with an admin user
#         client.post('/api/accounts/', self.admin_data, format='json')

#         # Get token user admin
#         token = client.post(
#             '/api/login/', self.admin_data_login, format='json'
#         ).json()['token']

#         client.credentials(HTTP_AUTHORIZATION='Token ' + token)

#         response = client.post(
#            '/api/levels/', self.level1_data, format='json')
#         self.assertTrue(response.status_code, 201)

#     def test_should_return_a_list_all_levels(self):
#         client = APIClient()

#         # Create a account admin
#         client.post('/api/accounts/', self.admin_data, format='json')

#         # Get token user admin
#         token = client.post(
#             '/api/login/', self.admin_data_login, format='json'
#         ).json()['token']

#         client.credentials(HTTP_AUTHORIZATION='Token ' + token)

#         response = client.get('/api/levels/')
#         self.assertTrue(response.status_code, 200)

#         # Create two levels
#         client.post(
#            '/api/levels/', self.level1_data, format='json')
#         client.post(
#            '/api/levels/', self.level2_data, format='json')

#         # Must contain two levels
#         get_all_levels = client.get('/api/levels/').json()
#         self.assertEqual(len(get_all_levels), 2)
