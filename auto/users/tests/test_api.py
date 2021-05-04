from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class SigninTestApi(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(email='stas.yyyy20gmail.com',
                                                         password='123',
                                                         )
        self.user.save()


