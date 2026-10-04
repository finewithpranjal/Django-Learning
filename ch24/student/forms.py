from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


#  Clean and valiate for a specific field
#     def clean_name(self):
#         # name_value = self.cleaned_data.get('name')
#         name_value = self.cleaned_data['name']
#         if len(name_value) < 4:
#             raise forms.ValidationError('Name must be at least 4 characters long.')
#         return name_value
    

#      def clean_email(self):
#          email_value = self.cleaned_data['email']
#          if len(email_value) < 20:
#              raise forms.ValidationError('Email must be at least 20 characters long.')
#          return email_value

    # Can make for multiple fields as well !!


# Clean and valiate Djanog form for all at once 
    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')
       
        if name_value and len(name_value) < 4:
            self.add_error('name', 'Name must be at least 4 characters long.')
            
        if email_value and len(email_value) < 20:
            self.add_error('email', 'Email must be at least 20 characters long.')

        return cleaned_data    