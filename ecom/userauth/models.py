from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)  # Ensure username is unique
    password = models.CharField(max_length=128, default='defaultpassword')
    bio=models.CharField(max_length=128,default='none')

    REQUIRED_FIELDS = ['email']  # Only email is required in addition to the username
    USERNAME_FIELD = 'username'  # This should be a string, not a list
    
    def __str__(self):
        return self.username