from .models import CustomUser
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)
def save_profile(sender, instance, **kwards):
    instance.profile.save()
