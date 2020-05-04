from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
