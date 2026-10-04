from django.shortcuts import render
from student.forms import Registration, Login  
 

def register(request):
    # fm = Registration()
    fm = Registration(field_order=['email', 'city'])
    return render(request, 'student/registration.html', {'form':fm})


def login(request):
    fm = Login()
    return render(request, 'student/login.html', {'form':fm})

