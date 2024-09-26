from django.contrib.auth.models import AbstractUser
from django.db import models

# Extending Django's built-in User model to include additional fields
class User(AbstractUser):
    # The id field is automatically created as the primary key by Django
    email = models.EmailField(unique=True)  # Email must be unique

    def __str__(self):
        return self.username  # Return the username for easy identification
