from django import forms
from django.forms import ModelForm
from carts.models import ShippingInformation

class ShippingForm(ModelForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    address_1 = forms.CharField(max_length=255, label='Address 1')
    address_2 = forms.CharField(max_length=255, required=False, help_text='Optional', label='Address 2')
    city = forms.CharField(max_length=255, label='City')
    postcode = forms.IntegerField(label='Postcode')
    country = forms.CharField(max_length=255, label='Country')

    class Meta:
        model = ShippingInformation
        fields = ('last_name', 'first_name', 'address_1', 'address_2', 'city', 'postcode', 'country')
