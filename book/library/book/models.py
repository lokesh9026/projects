from django.db import models

# Create your models here.
class Book (models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
