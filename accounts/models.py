from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Add any additional fields you want for your user model
    # For example, you can add a field for the user's email or profile picture
    email = models.EmailField(unique=True)

    # You can add more fields as per your requirements

    def __str__(self):
        return self.username
