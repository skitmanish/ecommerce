from django.db import models

class Add(models.Model):
    fname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    uname=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    address1=models.CharField(max_length=70)
    address2=models.CharField(max_length=70)
    country=models.CharField(max_length=70)
    state=models.CharField(max_length=70)
    zip=models.IntegerField(default=000000)
