from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager
from Configs.settings import *


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = PhoneNumberField(null=True, region='RU')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(_("First name"), max_length=200, blank=True)
    location = models.CharField(_("Location"),max_length=30, blank=True)

    def __str__(self):
        return f'профайл пользователя {self.user}'

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'
