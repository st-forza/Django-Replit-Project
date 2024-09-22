from django import forms
from django.contrib.auth.forms import AuthenticationForm


class NewLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"Placeholder":"Enter Username", "class": "form-control"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"Placeholder": "Enter Password","class": "form-control"}))

