from django.db import models


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    onSale = models.BooleanField()
    compatibility = models.CharField(max_length=999)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.name
