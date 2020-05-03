from django.db import models


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ExtraImages(models.Model):
    name = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=999)



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    onSale = models.BooleanField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    release_date = models.DateTimeField()
    product_display_image = models.CharField(max_length=999, null=True)
    extra_images = models.ManyToManyField(ExtraImages)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    url = models.CharField(max_length=999)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE) #<--- If Product gets deleted, all images get deleted beloning to the product id