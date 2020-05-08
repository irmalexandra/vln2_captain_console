from django.forms import ModelForm
from django import forms

from users.models import Review


class ReviewForm(ModelForm):
    CHOICES = [(True, 'Yes'),
               (False, 'No')]

    recommend = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    feedback = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Review
        fields = ('recommend', 'feedback')
