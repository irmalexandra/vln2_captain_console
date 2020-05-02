import datetime as datetime
from django.db import models

# Create your models here.
from django.utils.timezone import now

from main.models import Product


class PaymentInformation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=10)
    expiration_date = models.DateTimeField()
    cvv = models.CharField(max_length=5)

    def __str__(self):
        return self.first_name + " " + self.last_name


class ShippingInformation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return "Shipping information: " + self.first_name + " " + self.last_name


class Order(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.PROTECT)
    datetime = models.DateTimeField(default=now)
    shipping_information_id = models.ForeignKey(ShippingInformation, on_delete=models.PROTECT)
    Payment_information_id = models.ForeignKey(PaymentInformation, on_delete=models.PROTECT)

    def __str__(self):
        return "order made by " + self.Payment_information_id.__str__()
