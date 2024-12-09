from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CustomLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
