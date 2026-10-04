from django.shortcuts import render

def heydjango(req):
    return render(req, 'course/django.html' , {'name':'Django 5.x'})


  
def heypython(req):
    return render(req, 'course/python.html')
  
