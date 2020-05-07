from django import forms
from django.forms import ModelForm
from carts.models import PaymentInformation
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class EditPaymentForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    card_number = CardNumberField(required=True, label='Card Number')
    expiration_date = CardExpiryField(required=True, label='Expiration Date')
    cvv = SecurityCodeField(required=True, label='CVV/CVC')

    class Meta:
        model = PaymentInformation
        fields = ('last_name', 'first_name', 'card_number', 'expiration_date', 'cvv')
