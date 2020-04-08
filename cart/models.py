from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Cart(models.Model):
                         cartitem=ArrayField(ArrayField(models.IntegerField()))
                         user=models.CharField(max_length=30)
