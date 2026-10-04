from django import forms
from student.models import user

class Registration(forms.ModelForm):
    conferm_password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    class Meta:
        model = user
        # fields = ['username', 'password', 'email']
        fields = '__all__'
        labels = {'username' : 'Enter username', 'password' : 'Enter password', 'email' : 'Enter email'}
        error_messages = {
            'email' : {
                'required' : 'Email is required',
                'invalid' : 'Enter a valid email address'
            }
        }
        widgets = {
            'password': forms.PasswordInput()
        }