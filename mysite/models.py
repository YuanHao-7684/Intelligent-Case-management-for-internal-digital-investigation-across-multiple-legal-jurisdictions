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
class Cases(models.Model):
    caseId=models.BigAutoField(primary_key=True)
    caseUser=models.CharField(max_length=32)
    casetitle=models.CharField(max_length=128)
    caseContent=models.CharField(max_length=1024)
    caseOpencoutryNumber=models.CharField(max_length=6)
    caseNeutralcoutryNumber = models.CharField(max_length=6)
    caseStrcitcoutryNumber = models.CharField(max_length=6)
class SetUpCases(models.Model):
    caseId = models.BigAutoField(primary_key=True)
    caseUserName= models.CharField(max_length=32)
    UserInputId=models.CharField(max_length=32)
    caseName = models.CharField(max_length=32)
    caseScope = models.CharField(max_length=128)
    caseInv = models.CharField(max_length=128)
    caseInvEmail = models.CharField(max_length=128)
    caseType = models.CharField(max_length=128)
    casesynopsis = models.CharField(max_length=1000)
class Evidence(models.Model):
    EvidenceId = models.BigAutoField(primary_key=True)
    EvidenceName = models.CharField(max_length=32)
    ComCaseId = models.CharField(max_length=32)
    ComCaseName = models.CharField(max_length=32)
    EvidenceType = models.CharField(max_length=32)
    Principal = models.CharField(max_length=32)
    Source = models.CharField(max_length=32)
    EvidenceLoc = models.CharField(max_length=32)
    EvidenceSummary = models.CharField(max_length=1000)