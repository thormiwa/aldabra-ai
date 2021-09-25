import unittest
from django.test import Client

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.post(
        '/auth/login/',
        {
        'email': 'aamid@gmail.com',
        'password': 'passcodetest'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/')

    def get_settings(self):
        response = self.client.get('/settings/')

        self.assertEqual(response.status_code, 200)
