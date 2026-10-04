from django import forms
from django.core import validators


def start_with_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError('Email should start with S')

    
# Built-In Validators
class Registration(forms.Form):
    username = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(3)])
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    email = forms.EmailField(validators=[start_with_s])