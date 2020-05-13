from django.db import models


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ExtraImages(models.Model):
    name = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=999, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    on_sale = models.BooleanField()
    copies_sold = models.IntegerField(default=0)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    release_date = models.DateTimeField()
    product_display_image = models.CharField(max_length=999, null=True)
    extra_images = models.ManyToManyField(ExtraImages)
    discount = models.IntegerField(default=0, null=True)
    discount_price = models.IntegerField(default=False, null=True)

    url = "product"

    def __str__(self):
        return self.name

    def get_url(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.on_sale:
            self.discount_price = int(float(self.price) * (1.0-(self.discount/100)))
        else:
            self.discount_price = None
            self.discount = None
        super(Product, self).save(*args, **kwargs)


class ProductImages(models.Model):
    url = models.CharField(max_length=999)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE) #<--- If Product gets deleted, all images get deleted beloning to the product id