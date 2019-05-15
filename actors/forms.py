from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    score = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            })    
        )
    comment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            })
        )
    class Meta:
        model = Rating
        fields = ['score', 'comment']