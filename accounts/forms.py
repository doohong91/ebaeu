from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'nickname']
        widgets = {
            'description':forms.Textarea(attrs={'placeholder':'자기소개'}),
            'nickname':forms.TextInput(attrs={'placeholder':'닉네임'})
        }