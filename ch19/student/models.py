from django.db import models

class Profile (models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(default=0)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)

    # def __str__(self):
    #     return str(self.roll)

    
class Result (models.Model):
    stu_class = models.CharField(max_length=70)
    marks = models.IntegerField()

    # def __str__(self):
    #     return str(self.stu_class)
