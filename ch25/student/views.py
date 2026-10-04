from django.shortcuts import render
from student.forms import *
from django.http import HttpResponseRedirect


def register(req):
    if req.method == 'POST':    
        form = Registration(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            print('Username:', username)
            print('Password:', password)
            print('Email:', email)
            return HttpResponseRedirect('/student/register/')

    else :
        form = Registration()
    return render(req, 'student/register.html', {'form': form})
