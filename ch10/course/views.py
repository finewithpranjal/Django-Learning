from django.shortcuts import render

def heydjango(req):
    return render(req, 'course/django.html')


  
def heypython(req):
    return render(req, 'course/python.html')
  

