
# one to one relationship example
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.user_id 

# This model represents a user profile that is linked to a User model
# using a one-to-one relationship. Each user can have only one profile.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.username