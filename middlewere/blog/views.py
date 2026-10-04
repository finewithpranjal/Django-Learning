from django.shortcuts import render
from django.template.response import TemplateResponse


def home(req):
    print("home view called")
    return render(req, 'blog/home.html')


def math(req):
    print("math view called")
    a=10/2
    return render(req, 'blog/math.html', {'a': a})


def user_info(req):
    print('user_info view called')
    context = {'name' : 'Pranjal'}
    return render(req, 'blog/user.html', context)