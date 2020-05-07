from django import forms

from carts.models import CartItems


class CartItemsForm(forms.ModelForm):
    quantity = forms.IntegerField()
    productID = forms.IntegerField()
    price = forms.IntegerField()
    cartID = forms.IntegerField()

    class Meta:
        model = CartItems
        fields = (
            'quantity',
            'productID',
            'price',
            'cartID',
        )
