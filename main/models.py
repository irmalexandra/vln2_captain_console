from django.db import models


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    onSale = models.BooleanField()
    compatibility = models.CharField(max_length=999)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    release_date = models.DateTimeField()
