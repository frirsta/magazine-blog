from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Class that requests information from the user
    """
    email = models.EmailField('email adress', blank=False, unique=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    account_created = models.DateField(auto_now_add=True)
