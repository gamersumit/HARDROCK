from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):

    email = models.EmailField(unique=True, blank=False, null=False)
    is_admin = models.BooleanField(default = False)
    is_verified = models.BooleanField(default = False)
    phone_number = models.CharField(max_length=20, blank=False, null = False)
    username = models.CharField(max_length=50, blank=False, null = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    