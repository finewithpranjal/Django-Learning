from django.shortcuts import render
from django.http import HttpResponse

def myapp4(req):
    return HttpResponse(f',<h1>Hello App4</h1>')