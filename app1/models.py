from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):

    user_type = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    address = models.TextField()
    phone_no = models.CharField(max_length=15)


class Register(models.Model):
    
    donorname = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    unit = models.IntegerField()
    age = models.IntegerField()







    