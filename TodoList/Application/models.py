from django.db import models

# Create your models here.

class User:
    user_name = models.CharField(max_length=100, unique=True)