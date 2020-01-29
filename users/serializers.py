from rest_framework import serializers
from .models import CustomUser
from cars.models import Cars


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField(many=True)#  по related name  достаем  машины принадлежащие юзеру (см . def __str__)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'phone_number', 'car')
