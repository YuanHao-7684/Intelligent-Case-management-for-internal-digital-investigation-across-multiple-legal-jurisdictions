from django.db import models

# Create your models here.
class User (models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
