from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=20)
    gender = models.CharField(max_length=3)
    email =  models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username
