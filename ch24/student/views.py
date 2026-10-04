from django.shortcuts import render
from django.http import HttpResponseRedirect
from student.forms import *

def register(req):
    if req.method == 'POST':
        form = Registration(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('Name : ', name)
            print('Email : ', email)
            print('Password : ', password)
           
            return HttpResponseRedirect('/student/register/')  # Redirect to a success page
    else:
        form = Registration()
    return render(req, 'student/register.html', {'form': form})
