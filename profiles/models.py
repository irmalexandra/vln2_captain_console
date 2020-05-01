from django.db import models

# Create your models here.
from cart.models import Orders
from main.models import Reviews








class Profiles(models.Model):
    user = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.IntegerField(max_length=100)
    country = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=999)
    reviews = models.ForeignKey(Reviews)


class OrderHistory(models.Model):
    profileID = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Orders)


class Searches(models.Model):
    search = models.CharField(max_length=255)


class SearchHistory(models.Model):
    searchID = models.ForeignKey(Searches)
    profileID = models.ForeignKey(Profiles, on_delete=models.CASCADE)