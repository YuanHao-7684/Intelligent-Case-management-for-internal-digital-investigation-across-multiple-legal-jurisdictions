from django.db import models


# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=32)

class LawIno(models.Model):
    country = models.CharField(max_length=64)
    LawName = models.CharField(max_length=128)
    KeyPoint = models.CharField(max_length=1024)
    restrictedMode = models.CharField(max_length=16)
    AgreementCountry = models.CharField(max_length=1024, blank=True, null=True)
