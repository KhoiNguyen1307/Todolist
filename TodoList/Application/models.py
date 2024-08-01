from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=20)
    gender = models.CharField(max_length=3)
    email =  models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username

class Task(models.Model):
    userid = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()
    level = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
