from django.shortcuts import render
from django.http import HttpResponse

def myapp5(req):
    return HttpResponse(f'<h1>Hello App5</h1>')



