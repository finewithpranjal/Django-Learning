from django.shortcuts import render
from student.forms import *
from django.http import HttpResponseRedirect
from student.models import user

def register(req):
    if req.method == 'POST':    
        form = Registration(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            cpw = form.cleaned_data['conferm_password']
            print('username : ', username)
            print('password : ', password)
            print('email : ', email)
            print('Conferm_Password : ', cpw)

            user(username=username, password=password, email=email).save()

            return HttpResponseRedirect('/student/register/')

    else :
        form = Registration()
    return render(req, 'student/register.html', {'form': form})