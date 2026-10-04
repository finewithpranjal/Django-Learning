from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. mostly used for application logic,
# 2 types of views in Django:
# 1. Function-based views
# 2. Class-based views

def home(request):
    return HttpResponse('Home page')

def myfunction(request):
    return HttpResponse('HELLO WORLD!')

def render_html(request):
    return HttpResponse('<h1>This is a heading</h1>')

def learn_math(request):
    a = 10 + 20
    return HttpResponse(a)
