from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,unique=True)
    balance = models.IntegerField(default=0)
    date_joined = models.DateField(null=True,blank=True)
    profile_pic = models.ImageField(upload_to="profilepictures/", null=True, blank=True)

    first_name=None
    last_name=None



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class TokenTest(models.Model):
    randomCol = models.CharField(max_length=50)
