from django.forms import ModelForm, widgets
from users.models import Profile


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id' ]
        widgets = {
            'address': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'first_name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'last_name': widgets.TextInput(attrs={ 'class': 'form-control' })
        }