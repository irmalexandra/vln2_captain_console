from django.forms import ModelForm, widgets
from users.models import Profile
from django.contrib.auth.models import User


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('address_1', 'address_2', 'city', 'postcode', 'country', 'profile_image')
