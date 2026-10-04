from django.shortcuts import render
from school.models import *

def home(req):
    student_data = Student.objects.all()
    # student_data = Student.student.get_stu_roll_range(17, 33)

    context = {
        'student_data': student_data
    }

    return render(req, 'school/home.html', context)
