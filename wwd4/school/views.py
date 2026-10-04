from django.shortcuts import render
from school.models import Student
# from django.db.models import Q
# from django.db.models import Avg, Sum, Min, Max, Count

def home(req):
    # Limiting the queryset
    # students = Student.objects.all()[:3]  # This will limit the queryset to first 3 records

    # students = Student.objects.all()[2:5] # This will limit the queryset to records from index 2 to 4 (5 is exclusive)

    students = Student.objects.all()[:5:2] # This will limit the queryset to first 5 records and will take every second record

















    # From here we are staring Q objects in Django. for this you have to import Q from django.db.models. 

    # students = Student.objects.filter( Q(id=1) & Q(roll=21)) & IS FOR AND OPERATOR
    # students = Student.objects.filter( Q(id=1) | Q(roll=7)) | IS FOR OR OPERATOR
    # students = Student.objects.filter(~Q(id=1)) ~ IS FOR NOT OPERATOR
    # students = Student.objects.filter(Q(city='Indore') & Q(marks__gt=50))
    # students = Student.objects.filter(Q(city='Indore') | Q(marks__gt=50))

    # Below written code in comments is for aggregate functions contains average, sum, minimum, maximum and count of marks also we have to import Avg, Sum, Min, Max, Count from django.db.models to use these functions.

    # avg_marks = students.aggregate(Avg('marks'))
    # total = students.aggregate(Sum('marks'))
    # minimum = students.aggregate(Min('marks'))
    # maximum = students.aggregate(Max('marks'))
    # totalcount = students.aggregate(Count('marks'))
  
    context = {
         'students': students,
    #     'avg_marks': avg_marks,
    #     'total' : total,
    #     'minimum' : minimum,
    #     'maximum' : maximum,
    #     'totalcount' : totalcount

     }

   
    return render(req, 'school/home.html', context)
