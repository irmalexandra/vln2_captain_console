from django.forms import ModelForm
from django import forms

from users.models import Review


class ReviewForm(ModelForm):
    rating = forms.ChoiceField(choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"]])
    feedback = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Review
        fields = ('rating', 'feedback')
