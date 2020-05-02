from django.db import models

from consoles.models import Console
from main.models import Product


class Genre(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Game(Product):
    console_id = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True) # TODO: Rethink this one, chief


