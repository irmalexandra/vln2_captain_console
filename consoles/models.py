from django.db import models

# Create your models here.


class Specifications(models.Model):
    dimensions = models.CharField(max_length=100)
    weight = models.FloatField()
    connectivity = models.CharField(max_length=999)
    includes = models.CharField(max_length=999)
    storage_capacity = models.IntegerField()


class Consoles(models.Model):
    name = models.CharField(max_length=255)
    specification = models.ForeignKey(Specifications, on_delete=models.CASCADE)
    warranty = models.DateTimeField()
