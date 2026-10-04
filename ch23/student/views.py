from django.http import HttpResponseRedirect
from django.shortcuts import render
from student.forms import Registration



def register(req):
    if req.method == 'POST':
        fm = Registration(req.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            return HttpResponseRedirect('/student/success/')
            
    else:
        fm = Registration()
    return render(req, 'student/register.html', {'form':fm})


def thankyou(req):
    return render(req, 'student/success.html')