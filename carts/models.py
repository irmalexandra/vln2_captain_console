import datetime as datetime
from django.db import models

# Create your models here.


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
    datetime = models.DateTimeField(default=datetime.date.today())
    shipping_information_id = models.ForeignKey(ShippingInformation, on_delete=models.CASCADE)
    Payment_information_id = models.ForeignKey(PaymentInformation, on_delete=models.CASCADE)

    def __str__(self):
        return "order made by " + self.Payment_information_id.__str__()
