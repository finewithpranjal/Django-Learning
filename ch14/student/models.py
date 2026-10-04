from django.db import models

class Profile(models.Model): #Table banegi  
   name = models.CharField(max_length=70)      # |   column name hoga name aur uska type char hoga aur max length 70 hoga
   email = models.EmailField(max_length=255)
   city = models.CharField(max_length=70)
   roll = models.IntegerField()
   state = models.CharField(max_length=70)
   comment = models.CharField(max_length=255, default='Nothing')
#    student_profile --> is nam se table hoga 


 