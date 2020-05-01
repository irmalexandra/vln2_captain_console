from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=255)


class Manufacturers(models.Model):
    name = models.CharField(max_length=255)


class Plugs(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    quantity = models.IntegerField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField()
    #onSale = models.BooleanField()
    compatibility = models.ForeignKey(Plugs)
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    release_date = models.DateTimeField()


class Reviews(models.Model):
    profile = models.ForeignKey()
    rating = models.IntegerField(max_length=2)
    feedback = models.CharField(max_length=999)
    datetime = models.DateTimeField()
