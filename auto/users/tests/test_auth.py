from django.test import TestCase
from rest_framework.test import APITestCase,APIClient

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class SigninTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(email='stas.yyyy20gmail.com',
                                                         password='123',
                                                         )
        self.user.save()

    def test_correct(self):
        user = authenticate(email='stas.yyyy20gmail.com', password='123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(email='wrong@asd1', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(email='stas.yyyy20gmailcom', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def tearDown(self):
        self.user.delete()
