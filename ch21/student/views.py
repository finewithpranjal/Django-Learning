from django.shortcuts import render
from student.forms import Address, Registration
 

def registeration(request):
    fm = Registration()
    return render(request, 'student/registeration.html', {'form':fm})


def address(request):
    fm = Address()
    return render(request, 'student/address.html', {'form' : fm})
 

