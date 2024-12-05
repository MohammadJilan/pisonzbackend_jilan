from rest_framework import serializers
from .models import MyUser, TokenTest
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'balance', 'date_joined')

class TokenTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenTest
        fields = ('randomCol')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email
        token["balance"] = user.balance

        return token
