from django.contrib import admin

# Register your models here.
from consoles.models import Console
from main.models import Manufacturer

admin.site.register(Console)
admin.site.register(Manufacturer)