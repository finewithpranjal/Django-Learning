from django.shortcuts import render
from django.http import HttpResponse

def learn_dj(req):
    return HttpResponse(f'<h1>Hello Django</h1>')
