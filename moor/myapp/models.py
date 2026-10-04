from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT) # PROTECT prevents deletion of the user if a profile exists
    # user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}) # limit choices to staff users only
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=100)

class like(Page):
    # page = models.OneToOneField(Page, on_delete=models.CASCADE)
    likes = models.IntegerField()