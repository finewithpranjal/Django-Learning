from django import forms
from django.core.validators import MinLengthValidator

class DemoForm(forms.Form):
    # Basic fields
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()

    # Additional Field Types
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appointment_time = forms.TimeField()
    appointemnt_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    agree_terms = forms.NullBooleanField()

    # Choice Fields
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    interests = forms.MultipleChoiceField(choices=[('sports', 'Sports'), ('music', 'Music'), ('reading', 'Reading')])

    # File and URL Fields
    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()

    # Other Specialized Fields
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={'invalid': 'Enter a valid phone number.'})
    password = forms.CharField(widget=forms.PasswordInput())
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    rating = forms.DecimalField()