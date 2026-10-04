from django import forms
from django.core import validators


def start_with_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError('Email should start with S')

    
# Built-In Validators
class Registration(forms.Form):
    username = forms.CharField(error_messages={'required': 'Name is required'})
    password = forms.CharField(error_messages={'required': 'Password is required'},max_length=20, widget=forms.PasswordInput)
    email = forms.EmailField(error_messages={'required': 'Email should start with S'},validators=[start_with_s])