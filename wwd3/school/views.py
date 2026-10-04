from django.shortcuts import render
from school.models import Student

def home(req):
    # stu_d = Student.objects.all()
    # stu_d = Student.objects.filter(name="Raghav")
    # stu_d = Student.objects.filter(name__exact="Raghav")
    # stu_d = Student.objects.filter(name__iexact="Raghav") #Not case sensitive
    # stu_d = Student.objects.filter(name__contains="a") # find all names containing "a"
    # stu_d = Student.objects.filter(name__icontains="a")
    # stu_d = Student.objects.filter(id__in=[1,3,5]) # find all students with id 1,3,5
    # stu_d = Student.objects.filter(marks__gt=80) # find all students with marks greater than 80
    # stu_d = Student.objects.filter(marks__gte=80) # find all students with marks greater than or equal to 80
    # stu_d = Student.objects.filter(marks__lt=80) # find all students with marks less than 80
    # stu_d = Student.objects.filter(marks__lte=80) # find all students with marks less than or equal to 80
    # stu_d = Student.objects.filter(name__startswith="a") same as name__endswith="a" 
    stu_d = Student.objects.filter(name__startswith="a")
    print("Student Data:", stu_d)
    return render(req, 'school/home.html', {'students': stu_d})
