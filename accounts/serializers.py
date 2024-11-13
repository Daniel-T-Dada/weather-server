from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    
    class Meta:
        model = User
        fields = ("email", "password")


class WeatherUpdateSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = WeatherUpdate
        fields = "__all__"
