from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phonenumber = models.CharField(max_length=15,blank=True)