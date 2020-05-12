from django.db import models

from consoles.models import Console
from main.models import Product


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(Product):
    console_id = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre)
    copies_sold = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    url = 'games'


