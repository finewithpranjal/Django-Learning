from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()

    
