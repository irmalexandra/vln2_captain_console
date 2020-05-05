from django.forms import ModelForm
from users.models import Profile
from django.contrib.auth.models import User
from django import forms

class EditUserForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class EditProfileForm(ModelForm):
    address_1 = forms.CharField(max_length=30, required=False, help_text='Optional')
    address_2 = forms.CharField(max_length=30, required=False, help_text='Optional')
    city = forms.CharField(max_length=30, required=False, help_text='Optional')
    postcode = forms.IntegerField(required=False, help_text='Optional')
    country = forms.CharField(max_length=30, required=False, help_text='Optional')
    profile_image = forms.CharField(max_length=30, required=False, help_text='Optional')
    class Meta:
        model = Profile
        fields = ('address_1', 'address_2', 'city', 'postcode', 'country', 'profile_image')
