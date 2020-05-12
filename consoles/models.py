from django.db import models

# Create your models here.
from main.models import Product


class Console(Product):
    warranty = models.DateTimeField()
    specifications = models.TextField()

    url = "consoles"

