from django.db import models
from school.managers import CustomStudentManager


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    city = models.CharField(max_length=255)
    marks = models.IntegerField()
    pass_date = models.DateField()
    addmission_date = models.DateTimeField()

    objects = models.Manager()
    student = CustomStudentManager()  # custom manager we can use it in view function as Student.objects.all() or Student.objects.filter() etc.
    
 #objects = models.Manager()  # autometically created default manager we can change it and in view function we can use it as Student.objects.all() or Student.objects.filter() etc. we can create muliple managers such as student = models.Manager() and then we can use it as Student.student.all() or Student.student.filter() etc.
