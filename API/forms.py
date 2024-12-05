from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'date_joined', 'balance', 'profile_pic')  # Specify fields to include when creating a user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'balance', 'date_joined', 'profile_pic' , 'is_active', 'is_staff')  # Specify fields to include when editing a user
