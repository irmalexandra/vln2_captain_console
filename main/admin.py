from django.contrib import admin

# Register your models here.
from main.models import Manufacturer, ProductImages

admin.site.register(Manufacturer)
admin.site.register(ProductImages)
