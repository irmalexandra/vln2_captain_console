
from django.db import models
from creditcards.models import CardExpiryField, CardNumberField, SecurityCodeField
from django_countries.fields import CountryField
from django.utils.timezone import now

from main.models import Product


class PaymentInformation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    card_number = CardNumberField()
    expiration_date = CardExpiryField()
    cvv = SecurityCodeField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class ShippingInformation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.IntegerField()
    country = CountryField()

    def __str__(self):
        return "Shipping information: " + self.first_name + " " + self.last_name

    def raw_info(self):
        return str(self.first_name) + str(self.last_name) + str(self.address_1) + str(self.address_2) + str(self.city) + str(self.postcode) + str(self.country)


class Cart(models.Model):
    userID = models.IntegerField(null=True)
    check_out = models.BooleanField()
    date_created = models.DateTimeField(default=now)


class CartItems(models.Model):
    productID = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    cartID = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Order(models.Model):
    cartID = models.ForeignKey(Cart, on_delete=models.PROTECT)
    datetime = models.DateTimeField(default=now)
    shipping_information_id = models.ForeignKey(ShippingInformation, on_delete=models.PROTECT)
    payment_information_id = models.ForeignKey(PaymentInformation, on_delete=models.PROTECT)

    def __str__(self):
        return "order made by " + self.Payment_information_id.__str__()
