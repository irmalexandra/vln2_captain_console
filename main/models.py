from django.db import models
from profiles.models import Profiles
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=255)


class Manufacturers(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    quantity = models.IntegerField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField()
    #onSale = models.BooleanField()
    compatibility = models.CharField(max_length=999)
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    release_date = models.DateTimeField()



