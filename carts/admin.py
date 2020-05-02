from django.contrib import admin

# Register your models here.
from carts.models import Order, ShippingInformation, PaymentInformation

admin.site.register(Order)
admin.site.register(PaymentInformation)
admin.site.register(ShippingInformation)