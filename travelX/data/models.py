# models.py
from django.db import models

class Person (models.Model):
    fullname = models.CharField(max_length=50, null=True)
    dateofbirth = models.CharField(max_length=10, null=True)
    dlnumber = models.CharField(max_length=8, null=True)
