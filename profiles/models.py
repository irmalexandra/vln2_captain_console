from django.db import models

# Create your models here.
from carts.models import Orders
from games.models import Games







class Profiles(models.Model):
    user = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.IntegerField()
    country = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=999)



class Reviews(models.Model):
    profileID = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=999)
    datetime = models.DateTimeField()




class GameReviews(models.Model):
    gameID = models.ForeignKey(Games, on_delete=models.CASCADE)
    reviewID = models.ForeignKey(Reviews, on_delete=models.CASCADE)



class OrderHistory(models.Model):
    profileID = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE)


class Searches(models.Model):
    search = models.CharField(max_length=255)


class SearchHistory(models.Model):
    searchID = models.ForeignKey(Searches, on_delete=models.CASCADE)
    profileID = models.ForeignKey(Profiles, on_delete=models.CASCADE)


