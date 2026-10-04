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
            # Save data into database
            profile =  user(username=username, password=password, email=email)
            profile.save()
            return HttpResponseRedirect('/student/register/')
        
            # Update data into database
            # profile =  user(id = 1, username=username, password=password, email=email)
            # profile.save()

            # Delet data from database
            # profile =  user(id = 1)
            # profile.delete()
            

    else :
        form = Registration()
    return render(req, 'student/register.html', {'form': form})